#task2lesson20.py


"""
Write tests for the Phonebook application, which you have implemented in module 1. 
Design tests for this solution and write tests using unittest library
"""


import unittest
import json
import os
import sys


sys.path.append('./Phonebook')


from phonebook import load_phonebook, save_phonebook, add_record, delete_record, update_record, print_book, search_contact

class TestPhonebook(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_phonebook.json"
        self.phonebook = [
            {"number": "1234567890", "first_name": "John", "last_name": "Doe", "city": "New York", "state": "NY"},
            {"number": "0987654321", "first_name": "Jane", "last_name": "Smith", "city": "Los Angeles", "state": "CA"}
        ]
        save_phonebook(self.phonebook, self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_load_phonebook(self):
        loaded_phonebook = load_phonebook(self.test_file)
        self.assertEqual(loaded_phonebook, self.phonebook)

    def test_add_record(self):
        new_record = {"number": "1122334455", "first_name": "Alice", "last_name": "Johnson", "city": "Chicago", "state": "IL"}
        updated_phonebook = add_record(self.phonebook, **new_record)
        self.assertIn(new_record, updated_phonebook)

    def test_delete_record(self):
        deleted_record = delete_record(self.phonebook, "number", "1234567890")
        self.assertEqual(deleted_record, {"number": "1234567890", "first_name": "John", "last_name": "Doe", "city": "New York", "state": "NY"})
        self.assertNotIn(deleted_record, self.phonebook)

    def test_update_record(self):
        updated_record = update_record(self.phonebook, "number", "1234567890", "1111111111")
        self.assertEqual(updated_record["number"], "1111111111")

    def test_search_contact(self):
        result = search_contact(self.phonebook, "first_name", "John")
        self.assertEqual(result, "John        Doe          --- 1234567890")

    def test_print_book(self):
        with self.assertLogs(level='INFO') as log:
            print_book(self.phonebook, sort_by='last_name')
            self.assertIn("INFO:root:John        Doe          --- 1234567890", log.output)
            self.assertIn("INFO:root:Jane        Smith        --- 0987654321", log.output)

if __name__ == "__main__":
    unittest.main()
