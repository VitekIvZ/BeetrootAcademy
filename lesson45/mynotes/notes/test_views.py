import httpx
import asyncio
import time

# Базовий URL вашого Django-сервера
BASE_URL = "http://127.0.0.1:8000"

async def create_note():
    """Створює нову нотатку та повертає її ID."""
    async with httpx.AsyncClient() as client:
        # Отримуємо CSRF-токен
        csrf_response = await client.get(f"{BASE_URL}/notes/note/new/")
        csrf_token = csrf_response.cookies.get('csrftoken')
        
        # Дані для створення нотатки
        data = {
            "title": "Test Note",
            "text": "This is a test note.",
            "reminder": "1025-03-20 12:00:00",
            "category": "1",
        }
        
        # Відправляємо POST-запит для створення нотатки
        headers = {'X-CSRFToken': csrf_token}
        create_response = await client.post(f"{BASE_URL}/notes/note/new/", data=data, headers=headers)
        
        # Отримуємо ID створеної нотатки з відповіді сервера
        if create_response.status_code == 200:
            note_id = create_response.json().get('note', {}).get('id')
            if note_id:
                print(f"Created note with ID: {note_id}")
                return note_id
            else:
                raise ValueError("Failed to retrieve note ID from response.")
        else:
            raise ValueError(f"Failed to create note. Status code: {create_response.status_code}")

async def delete_note(note_id):
    """Видаляє нотатку за її ID."""
    async with httpx.AsyncClient() as client:
        try:
            # Отримуємо CSRF-токен
            csrf_response = await client.get(f"{BASE_URL}/notes/note/new/")
            csrf_token = csrf_response.cookies.get('csrftoken')
            
            # Відправляємо POST-запит для видалення нотатки
            headers = {'X-CSRFToken': csrf_token}
            delete_url = f"{BASE_URL}/notes/note/{note_id}/delete/"
            response = await client.post(delete_url, headers=headers)
            
            # Перевіряємо результат
            if response.status_code == 302:
                print(f"Note {note_id} deleted successfully!")
            else:
                print(f"Failed to delete note {note_id}. Status code: {response.status_code}")
        except Exception as e:
            print(f"Error deleting note {note_id}: {e}")

async def test_view(url, note_id):
    """Тестує конкретний view."""
    start_time = time.time()
    async with httpx.AsyncClient() as client:
        try:
            # Отримуємо CSRF-токен
            csrf_response = await client.get(f"{BASE_URL}/notes/note/new/")
            csrf_token = csrf_response.cookies.get('csrftoken')
            
            headers = {'X-CSRFToken': csrf_token}
            if url.endswith("/new/"):
                # Для створення нотатки
                data = {
                    "title": "Test Note",
                    "text": "This is a test note.",
                    "reminder": "2025-03-20 12:00:00",
                    "category": "1",
                }
                response = await client.post(url, data=data, headers=headers)
            elif "/edit/" in url:
                # Для редагування нотатки
                data = {
                    "title": "Updated Note",
                    "text": "This note has been updated.",
                    "reminder": "3025-03-20 12:00:00",
                    "category": "1",
                }
                response = await client.post(url, data=data, headers=headers)
            elif "/delete/" in url:
                # Для видалення нотатки
                response = await client.post(url, headers=headers)
            else:
                # Для головної сторінки
                response = await client.get(url)
            
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"View {url} took {elapsed_time:.2f} seconds (Status: {response.status_code})")
            return elapsed_time
        
        except Exception as e:
            print(f"Error testing {url}: {e}")
            return 0

async def main():
    # Створюємо нову нотатку та отримуємо її ID
    note_id = await create_note()
    if not note_id:
        print("Failed to create a note. Exiting.")
        return
    
    # URL-адреси для тестування з використанням отриманого ID
    urls = [
        f"{BASE_URL}/",  # home
        f"{BASE_URL}/notes/note/new/",  # create_note
        f"{BASE_URL}/notes/note/{note_id}/edit/",  # update_note
        f"{BASE_URL}/notes/note/{note_id}/delete/",  # delete_note
    ]
    
    # Тестуємо всі views
    total_time = 0
    for url in urls:
        elapsed_time = await test_view(url, note_id)
        total_time += elapsed_time
    print(f"Total time for all views: {total_time:.2f} seconds")
    
    note_id = note_id + 1
    await delete_note(note_id)
    
if __name__ == "__main__":
    asyncio.run(main())