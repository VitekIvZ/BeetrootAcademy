import unittest
from phonebook_oop import Book, Contact


class TestBook(unittest.TestCase):

    def setUp(self):
        self.BOOK = [
        {"firstname": "Bil", "secondname": "Gates", "number": "38033 9348021", "city": "New York"}, 
        {"firstname": "Mark", "secondname": "Zuckerberg", "number": "38045 9348024"}, 
        {"firstname": "Ilon", "secondname": "Mask", "number": "38077 9348024"},
        {"firstname": "Donald", "secondname": "Trump", "number": "38097 9348024"},
        ]
        print("\nRunning setUp method...")
        self.book = Book()
        self.book.create_book_from_dict(self.BOOK[:-1])
        # self.book_2 = Book('Grit','Angela Duckworth',447,16,0.15)

    def tearDown(self):
        print("Running tearDown method...")
        
    def test_add_contact(self):
        print("Running test_add_contact...")
        contact = Contact('38097 9348024', 'Donald', 'Trump')
        self.book.add_contact(contact)
        self.assertIn(contact, self.book.book)
        # self.assertEqual(self.book_2.get_reading_time(), f"{447*1.5} minutes")
    

if __name__=='__main__':
    unittest.main()