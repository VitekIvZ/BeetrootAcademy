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
    if rec not in phonebook:
        phonebook.append(rec)
    else:
        print("Record already exists.")
    save_phonebook(phonebook)
    return phonebook


#def search_value_by_key(phonebook, key, value):
#    for entry in phonebook:
#        if entry.get(key) == value:
#            return entry
#    return None
    

def delete_record(phonebook, key, value):
    for entry in phonebook:
        if entry.get(key) == value:
            phonebook.remove(entry)
            return entry
        
    return None       

def update_record(phonebook, key, old_value, new_value):
    for entry in phonebook:
        if entry.get(key) == old_value:
            entry[key] = new_value
            return entry
    
    return None

def print_book(phonebook, sort_by='last_name'):
    if sort_by:
        for rec in sorted(phonebook, key=lambda rec: rec[sort_by]):
            print(f"{rec.get('first_name'):12} {rec.get('last_name'):12}  --- {rec.get('number')}")

    
def search_contact(phonebook, key, value):
    def valid_input(entry, key, value):
        if isinstance(key, list) and isinstance(value, list):           #Перевіряє, чи відповідають всі ключі значенням, якщо key і value є списками.
            return all(entry.get(k) == v for k, v in zip(key, value))
        elif isinstance(key, list):                                     #Перевіряє, чи відповідає хоча б один ключ значенню, якщо key є списком.
            return any(entry.get(k) == value for k in key)
        else:                                                           #Перевіряє, чи відповідає значення ключу, якщо key не є списком.
            return entry.get(key) == value

    for entry in phonebook:
        if valid_input(entry, key, value):
            return f"{entry.get('first_name'):12} {entry.get('last_name'):12}  --- {entry.get('number')}"
    
    return "Record not found."


