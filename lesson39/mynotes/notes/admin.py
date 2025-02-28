from django.contrib import admin
from .models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')  # Поля, які відображаються в списку
    search_fields = ('title', 'content')    # Поля, за якими можна шукати
    list_filter = ('created_at',)           # Фільтри
    
#Note.objects.create(title="Перша нотатка", content="Це вміст першої нотатки.")
#Note.objects.create(title="Друга нотатка", content="Це вміст другої нотатки.")

admin.site.register(Note, NoteAdmin)
