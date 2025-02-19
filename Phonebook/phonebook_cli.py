import json
import sys
import os
from phonebook import *


def main(file_name="phonebook.json"):
    try:
        phonebook = load_phonebook(file_name="phonebook.json")
    except FileNotFoundError as e:
        print(e)
        return

    while True:
        print("\nPhonebook Menu:")
        print("0. Print all phonebook")
        print("1. Add new entry")
        print("2. Search by first name")
        print("3. Search by last name")
        print("4. Search by full name")
        print("5. Search by telephone number")
        print("6. Search by city or state")
        print("7. Delete a record")
        print("8. Update a record")
        print("9. Exit")
        
        choice = input("\nEnter your choice: ")

        match choice:
            
            case "0":
                print_book(phonebook)
            case "1":
                number, firstname, lastname, city, state = map(str, input("Enter number, first name, last name, city, state: ").split())
                add_record(phonebook, number, firstname, lastname, city, state)
            case "2":
                first_name = input("Enter first name: ")
                print(search_contact(phonebook, "first_name", first_name))
            case "3":
                last_name = input("Enter last name: ")
                print(search_contact(phonebook, "last_name", last_name))
            case "4":
                full_name = input("Enter full name: ")
                first_name, last_name = full_name.split()
                print(search_contact(phonebook, ["first_name", "last_name"], [first_name, last_name]))
            case "5":
                phone_number = input("Enter phone number: ")
                print(search_contact(phonebook, "number", phone_number))
            case "6":
                city_or_state = input("Enter city or state: ")
                print(search_contact(phonebook, ["city","state"], city_or_state))
            case "7":
                phone_number = input("Enter phone number to delete: ")
                deleted_record = delete_record(phonebook, "number", phone_number)
                if deleted_record:
                    print("Record deleted:", deleted_record) 
                else:
                    print("Record not found.") 
            case "8":
                old_phone_number, new_phone_number = map(str, input("Enter old and new phone number to update: ").split())
                updated_record = update_record(phonebook, "number", old_phone_number, new_phone_number)
                if updated_record:
                    print("Record updated:", updated_record)
                else:
                    print("Record not found.")
            case "9":
                save_phonebook(phonebook, file_name)
                print("Phonebook saved. Exiting.")
                break
            case __:
                print("Invalid choice. Please try again.")
            
            
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python phonebook_cli.py <phonebook_file>")
    else:
        main(sys.argv[1])
