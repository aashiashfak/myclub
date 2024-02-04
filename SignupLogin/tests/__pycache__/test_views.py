from django.test import TestCase,Client
from django.urls import reverse
from base.models import Products

class TestViews(TestCase):
    
    def test_index(self):
        client = Client()
        response = client.get(reverse('index'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')



