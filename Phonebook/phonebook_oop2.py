import json
import sys
import os
import io

class Contact:
    
    def __init__(self, number, firstname="", lastname="", city='', state=''):
        self.number = number  #  [("mobile", '908345345'), ("mobile", '2039820), ]
        self.firstname = firstname
        self.lastname = lastname
        self.city = city
        self.state = state

        self._create_full_name()

    def has_number(self, number): #Потрібно перевірити, чи number є рядком.
        if isinstance(number, str):
            return self.number == number
        elif isinstance(number, list):
            return any(t_num == number for _, t_num in self.number)

    def _create_full_name(self):
        self.fullname = self.firstname + ' ' + self.lastname

    def update(self, number='', firstname="", lastname="", city='', state=''):
        if number and number != self.number:
            self._update_number(number)
        # if firstname:

    def _update_number(self, new_number):
        # validate number
        if len(new_number) == 10 and new_number.isdigit():
            self.number = new_number
        else:
            raise Exception("Invalid number format")
            #print()
            # lod()
            # message("  ")

    def __str__(self):
        return f'{self.fullname:30} : {self.number}'

    # def __repr__(self):
    #     pass

    # def __lt__(self, other):
    #     return self.secondname < other.secondname

    def __eq__(self, other):
        return self.firstname == other.firstname and self.number == other.number and self.lastname == other.lastname

class JsonBook:

    def __init__(self, file_name='phonebook.json', file_path=os.getcwd()):
        self.file_name = file_name
        self.file_path = file_path
        self.full_path = os.path.join(file_path, file_name)

    def write_book(self, obj):
        with io.open(self.full_path, 'w') as fp:
            json.dump(obj, fp, indent=4)

    def read_book(self):
        if not os.path.exists(self.full_path):
            return []
        with io.open(self.full_path, 'r') as fp:
            obj = json.load(fp)
        return obj
    
    def add_contact_to_json(self, contact): #Метод add_contact_to_json додає об'єкт contact без конвертації його у словник. Потрібно конвертувати об'єкт contact у словник перед додаванням.
        book = self.read_book()
        book.append(contact.__dict__)
        self.write_book(book)
    

class BookIterator:
    def __init__(self, iter_obj):
        self.obj = iter_obj
        self.curr = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        self.curr += 1
        if self.curr <= len(self.obj.book):
            return self.obj[self.curr]
        else:
            raise StopIteration()
        
        
class Book:
    def __init__(self, sort_by='lastname', file_name='phonebook.json', file_path=os.getcwd()):
        self.__sort_by = sort_by
        self.json_converter = JsonBook(file_name=file_name, file_path=file_path)
        self.book = self._load_contacts()
        self.read_book = self.json_converter.read_book
        self.write_book = self.json_converter.write_book
        self.add_contact_to_json = self.json_converter.add_contact_to_json
        self._sort(sort_by=sort_by)

    def _load_contacts(self):
        book_dict_list = self.json_converter.read_book()
        contacts = []
        for record in book_dict_list:
            contact = self.create_contact(
                number=record['number'], 
                firstname=record['firstname'], 
                lastname=record['lastname'], 
                city=record.get('city', ''),
                state=record.get('state', '')
            )
            contacts.append(contact)
        return contacts
    
    @property
    def sort_by(self):
        return self.__sort_by
    
    @sort_by.setter
    def sort_by(self, sort_by):
        if isinstance(sort_by, str):
            if sort_by in ("firstname", "lastname", "number"):
                self.__sort_by = sort_by
            else:
                raise Exception(f"key {sort_by} does not exists")
        elif isinstance(sort_by, (tuple, list)):
            pass
        
    def create_contact(self, number='', firstname='', lastname='', city='', state=''):
        return Contact(
                number=number, 
                firstname=firstname, 
                lastname=lastname, 
                city=city,
                state=state)

    def create_book_from_dict(self, book_dict_list=None): 
        """
        book = [
        {"firstname": "Bil", "secondname": "Gates", "number": "380339348021", "city": "New York"}, 
        {"firstname": "Mark", "secondname": "Zuckerberg", "number": "380459348024"}, 
        {"firstname": "Ilon", "secondname": "Mask", "number": "380779348024"},

        ]
        """
        if not book_dict_list:
            book_dict_list = self.json_converter.read_book()
        for record in book_dict_list:
            contact = self.create_contact(
                number=record['number'], 
                firstname=record['firstname'], 
                lastname=record['lastname'], 
                city=record.get('city', ''),
                state=record.get('state', '')
            )
            self.book.append(contact)
        self._sort()

    def convert_to_dict_list(self):
        dict_list = []
        for contact in self.book:
            record = {
                'number': contact.number,
                'firstname': contact.firstname, 
                'lastname': contact.lastname, 
                'city': contact.city,
                'state': contact.state
            }
            dict_list.append(record)
        return dict_list

    def add_contact(self, contact):
        for cont in self.book:
            if contact == cont:
                return
        self.book.append(contact)
        self.add_contact_to_json(contact)
        self._sort()

    def _sort(self, sort_by=''):
        if sort_by in ("firstname", "lastname", "number"):
            self.book.sort(key=lambda contact: getattr(contact, sort_by))  # contact.__dict__[sort_by], , reverse=True
        # else:
        #     self.book.sort()

    def find_contact_by_number(self, number):
        #contact = None
        #idx = -1
        for idx, contact in enumerate(self.book):
            if contact.has_number(number):
                return contact, idx
        return None, -1

    def remove_contact(self, number):
        contact, idx = self.find_contact_by_number(number)
        if idx != -1:
            self.book.pop(idx)
            self.write_book(self.convert_to_dict_list())
            del contact

    def __del__(self):
        self.json_converter.write_book(self.convert_to_dict_list())
    
    def __str__(self):
        result = []
        for contact in self.book:
            result.append(str(contact))
        return '\n'.join(result)
    
    def __getitem__(self, idx):
        return self.book[idx-1]
    
    def __setitem__(self, idx, contact):
        self.book[idx-1] = contact
        
    def __iter__(self):
        # self.curr_idx = 0
        # return self
        return BookIterator(self)    
    
    def show_book(self, sort_by=''):
        self._sort(sort_by=sort_by)
        print(str(self))

    # sort_by = property(get_sort_by, set_sort_by, None, "")


if __name__ == '__main__':
    contact = Contact('380981234567', 'Vik', 'Zay', 'Kyiv', 'UA')
    #contact2 = Contact('0230987654', 'Bill', 'Gates')
    #if contact.has_number('0230987654'):  # contact.number == '0230987654' or contact.number2 == 
    #    print("Number already exists")
    #print(contact == contact2)
    
    BOOK = [
        {"firstname": "Bil", "lastname": "Gates", "number": "38033 9348021", "city": "New York", "state": "NY"}, 
        {"firstname": "Mark", "lastname": "Zuckerberg", "number": "38045 9348024", "city": "New York", "state": "NY"}, 
        {"firstname": "Ilon", "lastname": "Mask", "number": "38077 9348024", "city": "New York", "state": "NY"},
        {"firstname": "Donald", "lastname": "Trump", "number": "38097 9348024", "city": "New York", "state": "NY"},
        ]
    book2 = [
        { "number": "380441234567",
        "firstname": "John",
        "lastname": "Doe",
        "city": "New York",
        "state": "NY"
        },
        { "number": "380987654321",
        "firstname": "Jane",
        "lastname": "Smith",
        "city": "Los Angeles",
        "state": "CA"
        }
    ]
    # print(contact.__dict__.get('number'))

    book = Book(file_name='phonebook.json', file_path='/home/vitek/MyPython/Beetroot/Phonebook')
    #book.create_book_from_dict(book2)
    print(book.read_book())
    #book.write_book(BOOK)
    print()
    #print(book.read_book())
    #book.add_contact(contact)
    #print()
    #print(book.read_book())
    #print(list(book.find_contact_by_number('0230987654')))
    book.show_book()
    #print(book)
    #book.write_book(book.convert_to_dict_list())
    #print(book.sort_by)  # book.get_sort_by()
    #book.sort_by = "number"  # ("number",  "secondname")  # book.set_sort_by("number")
    #print(book.sort_by)
    #del book.sort_by
    print()
    # a = 10
    # print(a)
    # a = a + 10

    book.show_book(sort_by='number')
    #print()
    # book.show_book(sort_by='firstname')
    # print()
    # book.show_book(sort_by='secondname')

    # print(book)
    #print(book.book[0])
    # book.book[0] = contact

    # book[1] = contact

    #for cont in book.book:
    #    print(cont)
    # print(book[1], book[2], sep='\n')
    #book.remove_contact('0230987654')
    #print(book.book[0])
    print()
    #print(book.read_book())
    #book.show_book(sort_by='number')