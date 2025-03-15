import django
django.setup()

from django.urls import reverse
from rest_framework import status
from api.views import ListView
from django.test import TestCase
from django.contrib.auth.models import User 
from .models import Author, Book

class APITestCase(TestCase):
    def setUp(self):
        print('Start Test')
        self.author = Author.objects.create(name="Joe Cole")
        self.book1 = Book.objects.create(title="Original Title", publication_year="2023-01-01", author=self.author)
        user = User.objects.create(username="Ed", password="Edward@alx2025")
        self.client.login(username="Ed", password="Edward@alx2025")

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
        data = {"title": "MummyReturnsEdward"}
        response = self.client.patch(f'/api/books/update/{self.book1.id}/' ,data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_DeleteView(self):
        response = self.client.delete(f'/api/books/delete/{self.book1.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT )
        print(response.status_code)