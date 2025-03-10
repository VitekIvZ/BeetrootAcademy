from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('create-note/', views.create_note, name='create-note'),
    path('note/<int:pk>/', views.note_detail, name='note-detail'), 
    path('note/<int:pk>/update/', views.update_note, name='update-note'),
    path('note/<int:pk>/delete/', views.delete_note, name='delete-note'), 
    path('posts/', views.post_list, name='post-list'), 
    path('create-post/', views.create_post, name='create-post'),
    path('post/<int:pk>/', views.post_detail, name='post-detail'),
    path('post/<int:pk>/update/', views.update_post, name='update-post'),
    path('post/<int:pk>/delete/', views.delete_post, name='delete-post'),
]