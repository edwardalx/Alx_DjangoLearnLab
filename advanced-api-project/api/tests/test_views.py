import django
django.setup()

from rest_framework import status
from api.views import ListView
from django.test import TestCase

class ListViewTestCase(TestCase):
    def setUp(self):
        print('Start Test')

    def tearDown(self):
        print('After Test')

    def test_Try(self):
        print("Running Test")

    def test_list_views(self):
        response = self.client.get('/api/books/', )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
