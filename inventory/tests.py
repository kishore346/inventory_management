from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Item
from django.contrib.auth.models import User



class ItemTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.client.login(username="testuser", password="password")

        url = reverse('token_obtain_pair')
        response = self.client.post(url, {"username": "testuser", "password": "password"}, format='json')
        self.token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def test_create_item(self):
        url = reverse('item-create')
        data = {"name": "Item 1", "description": "Test description"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    def test_read_item(self):
        item = Item.objects.create(name="Item 1", description="Test description")

        url = reverse('item-detail', kwargs={'pk': item.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Item 1")
    def test_update_item(self):
        item = Item.objects.create(name="Item 1", description="Test description")

        url = reverse('item-detail', kwargs={'pk': item.id})
        data = {"name": "Updated Item", "description": "Updated description"}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        item.refresh_from_db()
        self.assertEqual(item.name, "Updated Item")
    def test_delete_item(self):
        item = Item.objects.create(name="Item 1", description="Test description")

        url = reverse('item-detail', kwargs={'pk': item.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertFalse(Item.objects.filter(id=item.id).exists())
    def test_unauthorized_access(self):
        self.client.logout()


        url = reverse('item-create')
        data = {"name": "Item 1", "description": "Test description"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
