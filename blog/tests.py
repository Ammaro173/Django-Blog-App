from django.test import TestCase
from django.urls import reverse
from rest_framework import status

# Create your tests here.


class TestArticleView(TestCase):
    def setUp(self):
        self.client.login(username="testuser", password="testpassword")

    def test_authentication_required(self):
        self.client.logout()  # logout testuser
        url = reverse("articles-list")
        # 403 is forbidden
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
