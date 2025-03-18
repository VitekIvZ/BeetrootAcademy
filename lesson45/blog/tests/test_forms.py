from django.test import TestCase
from django.urls import reverse


class PostFormTest(TestCase):
    
    def test_create_post_valid_form(self):
        data = {
            'title': "Test",
            'slug': 'test-slug',
            'body': "Test etst test"
        }

        response = self.client.post(reverse('post_create_url'), data=data)

        self.assertEqual(response.status_code, 302)