from django.urls import path

from .views import *


urlpatterns = [
    
    path('sync/', sync_fetch_posts_requests),
    path('async/', async_fetch_posts_aiohttp),
    path('async_httpx/', async_fetch_posts_httpx)

]
