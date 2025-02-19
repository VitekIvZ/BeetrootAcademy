import json


class Contact:
    
    def __init__(self, number, firstname="", secondname="", city=''):
        self.number = number
        self.firstname = firstname
        self.secondname = secondname
        self.city = city

        self._create_full_name()

    # def _

    def has_number(self, number):
        return self.number == number

    def _create_full_name(self):
        self.fullname = self.firstname + ' ' + self.secondname

    def update(self, number='', firstname="", secondname="", city=''):
        if number and number != self.number:
            self._update_number(number)
        # if firstname:

    def _update_number(self, new_number):
        # validate number
        if len(new_number) == 10 and new_number.isdigits():
            self.number = new_number
        else:
            raise Exception()
            print()
            # lod()
            # message("  ")

    def __str__(self):
        return f'{self.fullname:30} : {self.number}'

    # def __repr__(self):
    #     pass

    def __lt__(self, other):
        
        return self.secondname < other.secondname


class JsonBook:

    def __init__(self, file_name='book.json'):
        self.file_name = file_name

    def write_book(self, obj):
        with open(self.file_name, 'w') as fp:
            json.dump(obj, fp, indent=4)

    def read_book(self):
        with open(self.file_name, 'r') as fp:
            obj = json.load(fp)
        return obj
    

class Book:
    def __init__(self, contact_list=[], sort_by='secondname'):
        """
        book = [contact1, contact2, ]       [-1, 3, -4, 2, 5, -10]
        """
        self.book = contact_list
        self.sort_by = sort_by
        self.json_converter = JsonBook()
        if contact_list:
            self._sort()

    def create_book_from_dict(self, book_dict_list=None): 
        """
        book = [
        {"firstname": "Bil", "secondname": "Gates", "number": "380339348021", "city": "New York"}, 
        {"firstname": "Mark", "secondname": "Zuckerberg", "number": "380459348024"}, 

        ]
        """
        if not book_dict_list:
            book_dict_list = self.json_converter.read_book()
        for record in book_dict_list:
            contact = Contact(
                number=record['number'], 
                firstname=record['firstname'], 
                secondname=record['secondname'], 
                city=record.get('city', '')
            )
            self.book.append(contact)
        self._sort()

    def convert_to_dict_list(self):
        dict_list = []
        for contact in self.book:
            record = {}
            record['number'] = contact.number
            record['firstname'] = contact.firstname
            record['secondname'] = contact.secondname
            record['city'] = contact.city
            dict_list.append(record)
        return dict_list

    def add_contact(self, contact):
        self.book.append(contact)
        self._sort()

    def _sort(self, sort_par=''):
        if sort_par:
            pass # self.book.sort()
        else:
            self.book.sort()

    def find_contact_by_number(self, number):
        contact = None
        idx = -1
        for rec in self.book:
            if rec.has_number(number):

                break

        return contact, idx

    def remove_contact(self, number):
        idx = self.find_contact_by_number(number)
        contact = self.book.pop(idx)
        del contact

    def __del__(self):
        # self.json_converter.write_book(self.convert_to_dict_list())
        pass

    def __str__(self):
        result = []
        for contact in self.book:
            result.append(str(contact))
        return '\n'.join(result)


if __name__ == '__main__':
    contact = Contact('0230987654', 'Bill', 'Gates', 'New York')

    BOOK = [
        {"firstname": "Bil", "secondname": "Gates", "number": "380339348021", "city": "New York"}, 
        {"firstname": "Mark", "secondname": "Zuckerberg", "number": "380459348024"}, 
        ]

    print(contact)

    book = Book()
    book.create_book_from_dict(BOOK)

    print(book)
