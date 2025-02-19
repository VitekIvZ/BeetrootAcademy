import json


def create_phonebook(book, book_file="phonebook.json"):
    with open(book_file, "w") as file:
        json.dump(book, file, indent=4)
        

if __name__ == "__main__":
    book = [
        { "number": "380441234567",
        "first_name": "John",
        "last_name": "Doe",
        "city": "New York",
        "state": "NY"
        },
        { "number": "380987654321",
        "first_name": "Jane",
        "last_name": "Smith",
        "city": "Los Angeles",
        "state": "CA"
        }
    ]
    create_phonebook(book, "phonebook.json")
"""

Функція 

print_contact

 здійснює пошук і виведення записів у телефонному довіднику на основі заданих ключів і значень. Ось аналіз коду:

### Аналіз коду

1. **Параметри функції**:
   - 

phonebook

: список записів телефонного довідника.
   - 

key

: ключ або список ключів для пошуку.
   - 

value

: значення або список значень для пошуку.

2. **Перевірка довжини ключів і значень**:
   - Якщо довжина 

key

 і 

value

 дорівнює 2, функція перевіряє, чи відповідають обидва ключі обом значенням.
   - Якщо довжина 

key

 дорівнює 2, а довжина 

value

 не дорівнює 2, функція перевіряє, чи відповідає хоча б один з ключів значенню.
   - В іншому випадку функція перевіряє, чи відповідає значення ключу.

### Оптимізація коду

Функцію можна оптимізувати для кращої читабельності та уникнення повторення коду. Ось оптимізована версія:

```python


def print_contact(phonebook, key, value):
    def match(entry, key, value):
        if isinstance(key, list) and isinstance(value, list):
            return all(entry.get(k) == v for k, v in zip(key, value))
        elif isinstance(key, list):
            return any(entry.get(k) == value for k in key)
        else:
            return entry.get(key) == value

    for entry in phonebook:
        if match(entry, key, value):
            print(entry)

# Example usage
phonebook = [
    { "number": "380441234567",
      "first_name": "John",
      "last_name": "Doe",
      "city": "New York",
      "state": "NY"
    },
    { "number": "380987654321",
      "first_name": "Jane",
      "last_name": "Smith",
      "city": "Los Angeles",
      "state": "CA"
    }
]

# Search by first and last name
print_contact(phonebook, ["first_name", "last_name"], ["John", "Doe"])

# Search by city or state
print_contact(phonebook, ["city", "state"], "New York")

# Search by phone number
print_contact(phonebook, "number", "380987654321")
```

### Пояснення оптимізації:
1. **Функція `match`**:
   - Перевіряє, чи відповідають всі ключі значенням, якщо 

key

 і 

value

 є списками.
   - Перевіряє, чи відповідає хоча б один ключ значенню, якщо key є списком.
   - Перевіряє, чи відповідає значення ключу, якщо key не є списком.

2. **Основний цикл**:
   - Ітерується по кожному запису в телефонному довіднику.
   - Використовує функцію `match` для перевірки відповідності запису заданим ключам і значенням.
   - Виводить запис, якщо він відповідає умовам.

Ця оптимізована версія функції 

print_contact

 є більш читабельною і гнучкою для різних типів пошуку.

"""
