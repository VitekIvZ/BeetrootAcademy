import aiohttp, asyncio, requests, ssl, httpx
from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from time import time

from .models import TPost

# Create your views here.

def sync_fetch_posts_requests(request):

    start_time = time()

    TPost.objects.all().delete()

    response = requests.get(settings.API_URL, verify=True)
    post_data = response.json()

    for post in post_data:
        TPost.objects.create(
            id = post.get('id'),
            user_id = post.get('userId'),
            title = post.get('title'),
            body = post.get('body')
        )

    execution_time = time() - start_time

    return JsonResponse(
        {'message': f"Downloaded {len(post_data)} using requests", 
         'time': f"{execution_time}"}
    )   #  2.64 - 2.74


async def async_fetch_posts_aiohttp(request):

    start_time = time()

    await TPost.objects.all().adelete()

    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    async with aiohttp.ClientSession() as session:
        async with session.get(settings.API_URL, ssl=ssl_context) as response:
            post_data = await response.json()

    # tasks = [asyncio.create_task(TPost.objects.acreate(
    tasks = [TPost.objects.acreate(
                    id = post.get('id'),
                    user_id = post.get('userId'),
                title = post.get('title'),body = post.get('body'))
                for post in post_data]

    await asyncio.gather(*tasks)

    execution_time = time() - start_time

    return JsonResponse(
        {'message': f"Downloaded {len(post_data)} using aiohttp", 
         'time': f"{execution_time}"}
    )


async def async_fetch_posts_httpx(request):

    start_time = time()

    await TPost.objects.all().adelete()

    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    async with httpx.AsyncClient(verify=False) as client:
        response = await client.get(settings.API_URL)
        post_data = response.json()

    # tasks = [asyncio.create_task(TPost.objects.acreate(
    tasks = [TPost.objects.acreate(
                    id = post.get('id'),
                    user_id = post.get('userId'),
                title = post.get('title'),body = post.get('body'))
                for post in post_data]

    await asyncio.gather(*tasks)

    execution_time = time() - start_time

    return JsonResponse(
        {'message': f"Downloaded {len(post_data)} using httpx", 
         'time': f"{execution_time}"}
    )