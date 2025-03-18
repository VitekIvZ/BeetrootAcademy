from django.urls import path
from django.contrib import admin

from .views import *


urlpatterns = [
    # https://127.0.0.1:8000/ blog/ 
    path('', home_blog, name="home_blog_url"),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    # path('register/', register, name='register'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('posts/', Posts.as_view(), name='posts_list_url'),
    path('tags/', Tags.as_view(), name='tags_list_url'),
    path('post/create/', PostCreate.as_view(), name='post_create_url'),
    path('post/<slug>/', PostDetail.as_view(), name='post_detail_url'),
    path('post/<slug>/update/', PostUpdate.as_view(), name='post_update_url'),
    path('post/<slug>/delete/', PostDelete.as_view(), name='post_delete_url'),
    path('tag/create/', TagCreate.as_view(), name='tag_create_url'),
    path('tag/<slug>/', TagDetail.as_view(), name='tag_detail_url'),
    path('tag/<slug>/update/', TagUpdate.as_view(), name='tag_update_url'),
    path('tag/<slug>/delete/', TagDelete.as_view(), name='tag_delete_url'),

    # path('note/create', g_note),
    # path('note/<name>', n_note),
    # path('note/display/<int:id>', note),

]


admin.site.site_header = "Панель адміністрування"
admin.site.index_title = "Нотатник розробника"