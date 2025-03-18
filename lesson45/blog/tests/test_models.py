from django.test import TestCase
from django.shortcuts import redirect

from blog.models import Post, Tag


class TestPostModel(TestCase):

    @classmethod
    def setUpTestData(cls):
        Post.objects.create(title="Test", slug="test-slug", body="Test test test")

    def test_title_max_length(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('title').max_length
        self.assertEqual(max_length, 100)

    def test_slug_unique(self):
        post = Post.objects.get(id=1)
        unique = post._meta.get_field('slug').unique
        self.assertEqual(unique, True)

    def test_get_absolute_url(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.get_absolute_url(), # /blog/post/test-slug/
                         redirect('post_detail_url', post.slug).url)