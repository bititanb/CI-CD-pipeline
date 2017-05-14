import urlparse
from django.urls import reverse
from django.test import Client
from django.test import TestCase
from django.contrib.auth.models import User
from .models import *

class SimpleTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('test1', email='test1@example.com', password='password')
        # self.category = Category.objects.create(title="test-category1", user=self.user)
        # self.task = Task.objects.create(title='test-task1', body='test-body1', user=self.user, category=self.category, timeframe=1)

    def test_signup(self):
        url = reverse("account_signup")
        response = self.client.post(url, {'email': 'test2@example.com', 'password1': 'password', 'password2': 'password'}, follow=True)
        self.assertRedirects(response, reverse("tasklist"))

    def test_login(self):
        url = reverse("account_login")
        response = self.client.post(url, {'login': 'test1@example.com', 'password': 'password'}, follow=True)
        self.assertTrue(response.context['user'].is_active)
