from django.db import models

class Note(models.Model):
    CATEGORY_CHOICES = [
        ('Робота', 'Робота'),
        ('Особисте', 'Особисте'),
        ('Навчання', 'Навчання'),
    ]

    title = models.CharField(max_length=200, verbose_name="Назва")
    text = models.TextField(verbose_name="Текст")
    reminder = models.DateTimeField(null=True, blank=True, verbose_name="Нагадування")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, verbose_name="Категорія")

    def __str__(self):
        return self.title