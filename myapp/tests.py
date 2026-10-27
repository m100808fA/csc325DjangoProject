from django.test import TestCase

# test if the home view returns a 200 status code
class HomeViewTest(TestCase):
    def test_home_view_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

#test if the about view returns a 200 status code
class AboutViewTest(TestCase):
    def test_about_view_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)


#test if the home view returns the correct API endpoint response
class ApiHomeViewTest(TestCase):
    def test_api_home_view_response(self):
        response = self.client.get('/api/home/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "message": "Hello, World!",
            "description": "This is the home page of my Django application.",
        })

#test if the about view returns the correct API endpoint response
class ApiAboutViewTest(TestCase):
    def test_api_about_view_response(self):
        response = self.client.get('/api/about/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "message": "About",
            "description": "This is the about page of my Django application.",
        })