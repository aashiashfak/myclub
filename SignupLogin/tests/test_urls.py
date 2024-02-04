from django.test import SimpleTestCase
from django.urls import reverse, resolve
from base.views import home_page,signup,userlogin

class TestUrls(SimpleTestCase):
    def test_home_url(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, home_page)

    def test_signup_url(self):
        url = reverse('signup')
        self.assertEqual(resolve(url).func, signup)
    