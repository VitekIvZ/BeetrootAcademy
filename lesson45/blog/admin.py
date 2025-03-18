from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'body', 'published', 'modified', 'tags__title', 'brief_info')
    list_display_links = ('id', 'title')
    list_editable = ['body', ]
    list_per_page = 3
    search_fields = ['title', 'body']

    @admin.display(description="Стислий опис", ordering='body')
    def brief_info(self, post: Post):
        return f"Стаття містить {len(post.body)} сиволів"

# Register your models here.
# admin.site.register(Post, PostAdmin)
