from django.db import models

class Post(models.Model):
    user_id = models.IntegerField()
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.title
