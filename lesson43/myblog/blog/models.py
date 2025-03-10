from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

def validate_title_length(value):
    if len(value) < 5:
        raise ValidationError("Заголовок повинен містити щонайменше 5 символів.")

def validate_content_length(value):
    if len(value) < 20:
        raise ValidationError("Вміст повинен містити щонайменше 20 символів.")

class Post(models.Model):
    title = models.CharField(max_length=200, validators=[validate_title_length])
    content = models.TextField(validators=[validate_content_length])
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()  # Поле для вмісту нотатки
    date_created = models.DateTimeField(default=timezone.now)  # Поле для дати створення

    def __str__(self):
        return self.title
