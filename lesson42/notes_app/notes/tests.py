from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Note

class NoteAPITestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.note_data = {
            'title': 'Test Note',
            'text': 'This is a test note.',
            'reminder': '2023-12-31T23:59:59Z',
            'category': 'Робота'
        }
        self.note = Note.objects.create(**self.note_data)

    def test_create_note(self):
        url = reverse('note-list')
        response = self.client.post(url, self.note_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Note.objects.count(), 2)

    def test_get_note_list(self):
        url = reverse('note-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_note_detail(self):
        url = reverse('note-detail', args=[self.note.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.note_data['title'])

    def test_update_note(self):
        url = reverse('note-detail', args=[self.note.id])
        updated_data = {
            'title': 'Updated Note',
            'text': 'This note has been updated.',
            'reminder': '2023-12-31T23:59:59Z',
            'category': 'Особисте'
        }
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, updated_data['title'])

    def test_delete_note(self):
        url = reverse('note-detail', args=[self.note.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Note.objects.count(), 0)
