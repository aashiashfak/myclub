from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client
from base.models import Products

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.products = Products.objects.create(title='Product 1', price=10.99, image='path/to/image.png')

    def test_index_view_authenticated_user(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Access the index view
        response = self.client.get(reverse('index'))

        # Check that the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Check that the 'products' variable is present in the context
        self.assertIn('items', response.context)

        # Check that the products variable contains the expected product
        self.assertIn(self.products, response.context['items'])

