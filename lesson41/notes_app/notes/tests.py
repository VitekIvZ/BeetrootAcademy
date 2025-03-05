from django.test import TestCase
from .models import Note
from django.utils import timezone

class NoteModelTest(TestCase):
    def setUp(self):
        self.note = Note.objects.create(
            title="Тестова нотатка",
            text="Це текст тестової нотатки.",
            reminder=timezone.now(),
            category="Робота"
        )

    def test_note_creation(self):
        self.assertEqual(self.note.title, "Тестова нотатка")
        self.assertEqual(self.note.text, "Це текст тестової нотатки.")
        self.assertEqual(self.note.category, "Робота")
        self.assertIsNotNone(self.note.reminder)
        self.assertIsInstance(self.note.reminder, timezone.datetime)

    def test_note_str(self):
        self.assertEqual(str(self.note), "Тестова нотатка")

    def test_note_category_choices(self):
        choices = [choice[0] for choice in Note.CATEGORY_CHOICES]
        self.assertIn(self.note.category, choices)
