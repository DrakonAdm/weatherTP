from django.urls import reverse
from django.conf import settings
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import User
import os


class AdvertisementAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.superuser = User.objects.create_superuser(email='testuser@test.com', password='testpassword')
        self.user = User.objects.create_user(email='testNoSUPuser@test.com', password='testpassword')
        self.client.login(email='testuser@test.com', password='testpassword')
        self.url = reverse('advertisementPOST')
        self.image_path = os.path.join(settings.BASE_DIR, 'static', 'test_image.jpg')

    def test_upload_image(self):
        self.client.login(email='testNoSUPuser@test.com', password='testpassword')
        with open(self.image_path, 'rb') as f:
            response = self.client.post(self.url, {'file': f}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['success'], 'Image uploaded')

    def test_upload_image_unauthorized(self):
        self.client.logout()
        self.client.login(email='testNoSUPuser@test.com', password='testpassword')
        with open(self.image_path, 'rb') as f:
            response = self.client.post(self.url, {'file': f}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data['error'], 'Incorrect password')
        self.assertTrue(self.client.login(email='testuser@test.com', password='testpassword'))
        self.assertTrue(self.client.login(email='testNoSUPuser@test.com', password='testpassword'))


class ImageAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(email='testNoSUPuser@test.com', password='testpassword')
        self.url = reverse('advertisementGET')
        self.image_name = 'test_image.jpg'
        self.image_path = os.path.join(settings.STATIC_ROOT, 'image', self.image_name)

    def test_get_image(self):
        self.client.login(email='testNoSUPuser@test.com', password='testpassword')
        with open(self.image_path, 'rb') as f:
            response = self.client.get(f'{self.url}{self.image_name}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response['content-type'], 'image/jpeg')
        self.assertTrue(self.client.login(username='username', password='password'))

    def test_get_image_not_found(self):
        self.client.login(email='testNoSUPuser@test.com', password='testpassword')
        response = self.client.get(f'{self.url}nonexistent_image.jpg')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['error'], 'Image not found')
        self.assertTrue(self.client.login(username='username', password='password'))


