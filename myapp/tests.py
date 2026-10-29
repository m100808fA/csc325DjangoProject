from django.apps import apps
from django.test import TestCase
from django.urls import reverse

# add tests for the views and models here

class MyAppViewTests(TestCase):
    def test_home_page_returns_success_and_expected_content(self):
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello, World!")
        self.assertContains(response, "home page")

    def test_about_page_returns_success_and_expected_content(self):
        response = self.client.get(reverse('about'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "About")
        self.assertContains(response, "about page")

    def test_api_home_view_returns_success_and_expected_content(self):
        response = self.client.get(reverse('api_home'))

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {"message": "Hello, World!", 
             "description": "This is the home page of my Django application.",
             "version": "1.0.1",
            "date": "2026-10-28"
            }
        )

    def test_api_about_view_returns_success_and_expected_content(self):
        response = self.client.get(reverse('api_about'))

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {"message": "About", 
             "description": "This is the about page of my Django application.",
             "writer": "Muhammad Faseeh"
            }
        )

class MyAppModelTests(TestCase):
    def test_app_config_is_registered(self):
        app_config = apps.get_app_config('myapp')

        self.assertEqual(app_config.name, 'myapp')