from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('sign-up', views.sign_up, name='sign-up'),
    path('create-post', views.create_post, name='create-post'),
    path('update-post/<int:post_id>/', views.update_post, name='update-post'),
    path('delete-post/<int:post_id>/', views.delete_post, name='delete-post'),
    path('create-group/', views.create_group, name='create-group'),
    path('group/<int:group_id>/', views.group_detail, name='group-detail'),
    path('group/<int:group_id>/create-post/', views.create_post, name='create-group-post'),  # Змінено ім'я шляху
    path('post/<int:post_id>/', views.post_detail, name='post-detail'),
    path('groups/', views.group_list, name='group-list'),
    path('ban-user/<int:user_id>/', views.ban_user, name='ban-user'),
]
