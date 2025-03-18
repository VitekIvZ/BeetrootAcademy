from django.db import models
from django.urls import reverse

# Create your models here.

# .all()
# .filter(title='Post')  ->  
# .get(title='Post')  ->  exception

# class Chapter(models.Model):
#     name = models.CharField(max_length=100)


class Post(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name="Заголовок")
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField(blank=True, db_index=True, verbose_name="Текст")
    published = models.DateTimeField(auto_now_add=True, verbose_name="Опубліковано")
    modified = models.DateTimeField(auto_now=True, verbose_name="Змінено")
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts', verbose_name="Теги")
    # chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)  #

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Пости"

    def __repr__(self):
        return f"<{self.__class__.__name__}: id={self.pk}, title: {self.title:10}>"
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={"slug": self.slug})
    

class Tag(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    # posts = models.ManyToManyField(Post, blank=True, related_name='tags')

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={"slug": self.slug})
    
    def __str__(self):
        return f"{self.title}"
