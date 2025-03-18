from django.test import TestCase, Client

from django.contrib.auth import get_user_model


User = get_user_model()


class TestStaticUrls(TestCase):

    @classmethod
    def setUpClass(cls):
        return super().setUpClass()
    
    def setUp(self):
        self.quest_client = Client()
        # self.user = User.objects.create_user(username="TestUser")
        # self.authorized_client = Client()
        # self.authorized_client.force_login(self.user)

    def test_home_blog(self):
        response = self.quest_client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        
    def test_home_blog_template(self):
        response = self.quest_client.get('/blog/')
        self.assertTemplateUsed(response, 'blog/base_blog.html', "Template error")

    def test_urls_correct_templates(self):
        temlates = {
            '/blog/': "blog/base_blog.html",
            '/blog/posts/': "blog/posts.html", 
            # 'blog/tags/': "blog/tags.html"
        }

        for address, template in temlates.items():
            with self.subTest(address=address):
                response = self.quest_client.get(address)
                error_message = f"Error: {address} expects {template}"
                self.assertTemplateUsed(response, template)