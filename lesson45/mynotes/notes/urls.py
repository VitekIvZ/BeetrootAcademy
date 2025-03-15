from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('note/new/', views.create_note, name='create-note'),
    path('note/<int:note_id>/edit/', views.update_note, name='update-note'),
    path('note/<int:note_id>/delete/', views.delete_note, name='delete-note'),
    
]
