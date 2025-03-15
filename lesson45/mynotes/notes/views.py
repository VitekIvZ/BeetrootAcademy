# from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
# from .models import Note
# from .forms import NoteForm
# from django.contrib.auth.decorators import login_required
# from django.http import JsonResponse


# def home(request):
#     notes = Note.objects.all()
#     return render(request, 'notes/home.html', {'notes': notes})

# #@login_required
# def create_note(request):
#     if request.method == 'POST':
#         form = NoteForm(request.POST)
#         if form.is_valid():
#             note = form.save()
#             return JsonResponse({"status": "success", "note": {"id":note.id}})
#         else:
#             return JsonResponse({"status": "error", "errors": form.errors})
#     else:
#         form = NoteForm()
#     return render(request, 'notes/note_form.html', {'form': form})

# #@login_required
# def update_note(request, note_id):
#     note = get_object_or_404(Note, id=note_id)  # Отримуємо нотатку або 404
    
#     if request.method == 'POST':
#         form = NoteForm(request.POST, instance=note)  # Оновлюємо форму з даними
#         if form.is_valid():
#             updated_note = form.save()  # Зберігаємо оновлену нотатку
#             return JsonResponse({
#                 "status": "success",
#                 "message": "Note updated successfully!",
#                 "note": {
#                     "id": updated_note.id,
#                     "title": updated_note.title,
#                     "text": updated_note.text,  # Використовуємо оновлену нотатку
#                     "reminder": updated_note.reminder.strftime('%Y-%m-%d %H:%M:%S') if updated_note.reminder else None,
#                     "category": updated_note.category.id if updated_note.category else None,
#                 }
#             })
#         else:
#             # Якщо форма не валідна, повертаємо помилки
#             return JsonResponse({
#                 "status": "error",
#                 "message": "Invalid data",
#                 "errors": form.errors
#             }, status=400)
    
#     else:
#         # Для GET-запиту повертаємо поточні дані нотатки
#         return JsonResponse({
#             "status": "success",
#             "note": {
#                 "id": note.id,
#                 "title": note.title,
#                 "text": note.text,
#                 "reminder": note.reminder.strftime('%Y-%m-%d %H:%M:%S') if note.reminder else None,
#                 "category": note.category.id if note.category else None,
#             }
#         })

# #@login_required
# def delete_note(request, note_id):
#     note = get_object_or_404(Note, id=note_id)
#     if request.method == 'POST':
#         note.delete()
#         return redirect('home')
#     return render(request, 'notes/note_confirm_delete.html', {'note': note})

import aiohttp, asyncio, requests, ssl, httpx
import logging
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from .models import Note, Category
from .forms import NoteForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from asgiref.sync import sync_to_async

# Допоміжні функції для синхронізації
sync_get_object_or_404 = sync_to_async(get_object_or_404, thread_sensitive=True)
sync_get_list_or_404 = sync_to_async(get_list_or_404, thread_sensitive=True)
sync_render = sync_to_async(render, thread_sensitive=True)
sync_redirect = sync_to_async(redirect, thread_sensitive=True)
logger = logging.getLogger(__name__)

async def home(request):
    notes = await sync_to_async(list)(Note.objects.all())
    return await sync_render(request, 'notes/home.html', {'notes': notes})

#@login_required
@csrf_exempt
async def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            try:
                # Використовуємо acreate для асинхронного створення об'єкта
                logger.debug("Form data: %s", form.cleaned_data)
                note = await Note.objects.acreate(
                    title=form.cleaned_data['title'],
                    text=form.cleaned_data['text'],
                    reminder=form.cleaned_data['reminder'],
                    category = await sync_get_object_or_404(Category, id=form.cleaned_data['category'].id)
                )
                #await asyncio.gather(note)
                return JsonResponse({"status": "success", "note": {"id": note.id}})
            except Exception as e:
                logger.error("Error creating note: %s", str(e))
                return JsonResponse({"status": "error", "message": str(e)}, status=500)
        else:
            return JsonResponse({"status": "error", "errors": form.errors}, status=400)
    elif request.method == 'GET':
        # Повертаємо форму для створення нотатки
        form = NoteForm()
        return await sync_render(request, 'notes/note_form.html', {'form': form})
    else:
        return JsonResponse({"status": "error", "message": "Method not allowed"}, status=405)

#@login_required
@csrf_exempt
async def update_note(request, note_id):
    note = await sync_get_object_or_404(Note, id=note_id)
    
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            updated_note = await sync_to_async(form.save)()
            return JsonResponse({
                "status": "success",
                "message": "Note updated successfully!",
                "note": {
                    "id": updated_note.id,
                    "title": updated_note.title,
                    "text": updated_note.text,
                    "reminder": updated_note.reminder.strftime('%Y-%m-%d %H:%M:%S') if updated_note.reminder else None,
                    "category": updated_note.category.id if updated_note.category else None,
                }
            })
        else:
            return JsonResponse({
                "status": "error",
                "message": "Invalid data",
                "errors": form.errors
            }, status=400)
    
    else:
        return JsonResponse({
            "status": "success",
            "note": {
                "id": note.id,
                "title": note.title,
                "text": note.text,
                "reminder": note.reminder.strftime('%Y-%m-%d %H:%M:%S') if note.reminder else None,
                "category": note.category.id if note.category else None,
            }
        })

#@login_required
@csrf_exempt
async def delete_note(request, note_id):
    note = await sync_get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        await sync_to_async(note.delete)()
        return await sync_redirect('home')
    return await sync_render(request, 'notes/note_confirm_delete.html', {'note': note})

