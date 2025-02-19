# task11_2.py


"""
Extend Phonebook application

Functionality of Phonebook application:

    Add new entries +
    Search by first name 
    Search by last name 
    Search by full name
    Search by telephone number
    Search by city or state
    Delete a record for a given telephone number
    Update a record for a given telephone number
    An option to exit the program

The first argument to the application should be the name of the phonebook. 
Application should load JSON data, if it is present in the folder with application, else raise an error. 
After the user exits, all data should be saved to loaded JSON.
"""

import json
import sys
import os


def load_phonebook(file_name="phonebook.json"): 
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            obj = json.load(file)
        return obj
    else:
        raise FileNotFoundError(f"No such file: '{file_name}'")


def save_phonebook(phonebook, file_name="phonebook.json"):
    with open(file_name, "w") as file:
        json.dump(phonebook, file, indent=4)


def add_record(phonebook, number='', firstname='', lastname='', city="", state=''):
    rec = { "number": number,
        "first_name": firstname,
        "last_name": lastname,
        "city": city,
        "state": state
        }
    phonebook.append(rec)
    return phonebook


def search_value_by_key(phonebook, key, value):
    for entry in phonebook:
        if entry.get(key) == value:
            return entry
    return None
    

def delete_record(phonebook, key, value):
    for entry in phonebook:
        if entry.get(key) == value:
            phonebook.remove(entry)
            return phonebook
        print("Record deleted.") #прибрати
    else:
        print("Record not found.") #прибрати

def update_record(phonebook, key, old_value, new_value):
    for entry in phonebook:
        if entry.get(key) == old_value:
            entry[key] = new_value
            return entry
    return None

def print_book(phonebook, sort_by='lastname'):
    if sort_by:
        for rec in sorted(book, key=lambda rec: rec[sort_by]):
            print(f"{rec.get('firstname'):12} {rec.get('lastname'):12}  --- {rec.get('number')}")

    
def print_contact(phonebook, key, value):
    def valid_input(entry, key, value):
        if isinstance(key, list) and isinstance(value, list):           #Перевіряє, чи відповідають всі ключі значенням, якщо key і value є списками.
            return all(entry.get(k) == v for k, v in zip(key, value))
        elif isinstance(key, list):                                     #Перевіряє, чи відповідає хоча б один ключ значенню, якщо key є списком.
            return any(entry.get(k) == value for k in key)
        else:                                                           #Перевіряє, чи відповідає значення ключу, якщо key не є списком.
            return entry.get(key) == value

    for entry in phonebook:
        if valid_input(entry, key, value):
            print(entry)   

def main(file_name="phonebook.json"):
    try:
        phonebook = load_phonebook(file_name="phonebook.json")
    except FileNotFoundError as e:
        print(e)
        return

    while True:
        print("\nPhonebook Menu:")
        print("1. Add new entry")
        print("2. Search by first name")
        print("3. Search by last name")
        print("4. Search by full name")
        print("5. Search by telephone number")
        print("6. Search by city or state")
        print("7. Delete a record")
        print("8. Update a record")
        print("9. Exit")
        choice = input("Enter your choice: ")

        #match choice:

        if choice == "1":
            number, firstname, lastname, city, state = map(str, input("Enter number, first name, last name, city, state: ").split())
            add_record(phonebook, number, firstname, lastname, city, state)
        elif choice == "2":
            first_name = input("Enter first name: ")
            print_contact(phonebook, "first_name", first_name)
        elif choice == "3":
            last_name = input("Enter last name: ")
            print_contact(phonebook, "last_name", last_name)
        elif choice == "4":
            full_name = input("Enter full name: ")
            first_name, last_name = full_name.split()
            print_contact(phonebook, ["first_name", "last_name"], [first_name, last_name])
        elif choice == "5":
            phone_number = input("Enter phone number: ")
            print_contact(phonebook, "number", phone_number)
        elif choice == "6":
            city_or_state = input("Enter city or state: ")
            print_contact(phonebook, ["city","state"], city_or_state)
        elif choice == "7":
            phone_number = input("Enter phone number to delete: ")
            delete_record(phonebook, "number", phone_number)
        elif choice == "8":
            old_phone_number, new_phone_number = map(str, input("Enter old and new phone number to update: ").split())
            update_record(phonebook, "number", old_phone_number, new_phone_number)
        elif choice == "9":
            save_phonebook(phonebook, file_name)
            print("Phonebook saved. Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")
            
            
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python task11_2.py <phonebook_file>")
    else:
        main(sys.argv[1])
