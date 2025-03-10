from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from .forms import NoteForm
from django.contrib import messages
from .models import Note
from django.core.paginator import Paginator

def home(request):
    notes_list = Note.objects.all().order_by('-date_created')
    paginator = Paginator(notes_list, 5)  # 5 нотаток на сторінці
    page_number = request.GET.get('page')
    notes = paginator.get_page(page_number)
    return render(request, 'blog/home.html', {'notes': notes})

def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Нотатку успішно створено!')
            return redirect('blog-home')  # Повернення на головну сторінку
    else:
        form = NoteForm()
    return render(request, 'blog/create_note.html', {'form': form})

def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)  # Отримуємо нотатку за ID
    return render(request, 'blog/note_detail.html', {'note': note})

def update_note(request, pk):
    note = get_object_or_404(Note, pk=pk)  # Отримуємо нотатку за ID
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)  # Заповнюємо форму даними нотатки
        if form.is_valid():
            form.save()  # Зберігаємо оновлену нотатку
            messages.success(request, 'Нотатку успішно оновлено!')
            return redirect('note-detail', pk=note.id)  # Перенаправляємо на сторінку нотатки
    else:
        form = NoteForm(instance=note)  # Заповнюємо форму даними нотатки
    return render(request, 'blog/update_note.html', {'form': form})

def delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk)  # Отримуємо нотатку за ID
    if request.method == 'POST':  # Перевіряємо, чи це POST-запит
        note.delete()  # Видаляємо нотатку
        messages.success(request, 'Нотатку успішно видалено!')
        return redirect('blog-home')  # Перенаправляємо на головну сторінку
    return redirect('note-detail', pk=note.id)  # Якщо це не POST, повертаємо на сторінку нотатки

def post_list(request):
    posts = Post.objects.all().order_by('-date_posted')
    return render(request, 'blog/post_list.html', {'posts': posts})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Пост успішно створено!')
            return redirect('post-list')
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)  
    return render(request, 'blog/post_detail.html', {'post': post})

def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)  
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)  
        if form.is_valid():
            form.save()  
            messages.success(request, 'Пост успішно оновлено!')
            return redirect('post-detail', pk=post.id)  
    else:
        form = PostForm(instance=post)  
    return render(request, 'blog/update_post.html', {'form': form})

def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)  
    if request.method == 'POST':  # Перевіряємо, чи це POST-запит
        post.delete() 
        messages.success(request, 'Пост успішно видалено!')
        return redirect('blog-home')  
    return redirect('post-detail', pk=post.id)  


