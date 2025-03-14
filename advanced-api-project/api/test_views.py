import django
django.setup()

from django.urls import reverse
from rest_framework import status
from api.views import ListView
from django.test import TestCase
from .models import Author

class ListCreateUpdateViewsTestCase(TestCase):
    def setUp(self):
        print('Start Test')
        self.author = Author.objects.create(name="Joe Cole")

    def tearDown(self):
        print('After Test')

    def test_CreateView(self):
       data = { "title": "MummyReturns","publication_year":"2024-03-14","author": self.author.id }
       response = self.client.post('/api/books/create', data)
       self.assertEqual(response.status_code, status.HTTP_201_CREATED)
       print(response.data)
    
    def test_url_in_test(self):
        url = reverse('create-books')  # Replace 'create_book' with your URL name
        response = self.client.get(url)
        print(response.status_code)

    def test_ListViews(self):
        response = self.client.get('/api/books/', )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.status_code)
        print(response.data)

    def test_UpdateView(self):
        response = self.client.put('/api/books/update/')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_DeleteView(self):
        response = self.client.delete('/api/books/delete/')
        self.assertEqual(response.status_code, status.HTTP_200_OK )