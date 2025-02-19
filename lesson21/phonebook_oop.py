import os
import json


class Contact:
    
    def __init__(self, number, firstname="", secondname="", city=''):
        self.number = number  #  [("mobile", '908345345'), ("mobile", '2039820), ]
        self.firstname = firstname
        self.secondname = secondname
        self.city = city

        self._create_full_name()

    # def _

    def has_number(self, number):
        if isinstance(number, str):
            return self.number == number
        elif isinstance(number, list):
            return any(t_num == number for _, t_num in self.number)

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

    # def __lt__(self, other):
    #     return self.secondname < other.secondname

    def __eq__(self, other):
        return self.firstname == other.firstname and self.number == other.number and self.secondname == other.secondname


class JsonBook:

    def __init__(self, file_name='book.json'):
        self.file_name = file_name
        self.is_file = False
        if os.path.exists(file_name):
            self.is_file = True

    def write_book(self, obj, indent=4):
        with open(self.file_name, 'w') as fp:
            json.dump(obj, fp, indent=indent)

    def read_book(self):
        if self.is_file:
            with open(self.file_name, 'r') as fp:
                obj = json.load(fp)
            return obj
        else:
            raise FileNotFoundError()
    

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

    def __init__(self, contact_list=[], sort_by='secondname', file_name='book.json'):
        """
        book = [contact1, contact2, ]    
        """
        self.book = contact_list
        self.__sort_by = sort_by
        self.json_converter = JsonBook()
        self.file = None
        self.file_name = file_name
        if contact_list:
            self._sort(sort_by=sort_by)

    # def get_sort_by(self):
    #     return self.__sort_by
    
    # def set_sort_by(self, sort_by):
    #     if isinstance(sort_by, str):
    #         if sort_by in ("firstname", "secondname", "number"):
    #             self.__sort_by = sort_by
    #         else:
    #             raise Exception(f"key {sort_by} does not exists")
    #     elif isinstance(sort_by, (tuple, list)):
    #         pass

    @property
    def sort_by(self):
        return self.__sort_by
    
    @sort_by.setter
    def sort_by(self, sort_by):
        if isinstance(sort_by, str):
            if sort_by in ("firstname", "secondname", "number"):
                self.__sort_by = sort_by
                self._sort()
            else:
                raise Exception(f"key {sort_by} does not exists")
        elif isinstance(sort_by, (tuple, list)):
            pass
        
    def create_contact(self, number='', firstname='', secondname='', city=''):
        return Contact(
                number=number, 
                firstname=firstname, 
                secondname=secondname, 
                city=city)

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
                secondname=record['secondname'], 
                city=record.get('city', '')
            )
            self.book.append(contact)
        self._sort()

    def convert_to_dict_list(self):
        dict_list = []
        for contact in self.book:
            record = {
                'number': contact.number,
                'firstname': contact.firstname, 
                'secondname': contact.secondname, 
                'city': contact.city
            }
            # record['number'] = contact.number
            # record['firstname'] = contact.firstname
            # record['secondname'] = contact.secondname
            # record['city'] = contact.city
            dict_list.append(record)
        return dict_list

    def add_contact(self, contact):
        for cont in self.book:
            if contact == cont:
                return
        self.book.append(contact)
        self._sort()

    def _sort(self, sort_by=''):
        if sort_by in ("firstname", "secondname", "number"):
            self.book.sort(key=lambda contact: getattr(contact, sort_by))  # contact.__dict__[sort_by], , reverse=True
        else:
            self.book.sort(key=lambda contact: getattr(contact, "secondname"))

    def find_contact_by_number(self, number):
        # contact = None
        # idx = -1
        for idx, contact in enumerate(self.book):
            if contact.has_number(number):
                break
        return contact, idx

    def remove_contact(self, number):
        idx = self.find_contact_by_number(number)
        contact = self.book.pop(idx)
        del contact

    def save_to_json(self):
        self.json_converter.write_book(self.convert_to_dict_list(), indent=4)

    def __del__(self):
        # self.json_converter.write_book(self.convert_to_dict_list())
        pass

    def __str__(self):
        result = []
        for contact in self.book:
            result.append(str(contact))
        return '\n'.join(result)
    
    def __getitem__(self, idx):
        if isinstance(idx, slice):
            print(type(idx))
            start = idx.start - 1 if idx.start is not None else idx.start
            stop = idx.stop - 1 if idx.stop is not None else idx.stop
            step = idx.step
            return self.book[start:stop:step]  # [:10] => 1, 10, None  [::-1]
        return self.book[idx-1]
    
    def __setitem__(self, idx, contact):   # self.book[idx] = ,   
        self.book[idx-1] = contact

    def __iter__(self):
        # self.curr_idx = 0
        # return self
        return BookIterator(self)
    
    def __contains__(self, contact):
        return contact in self.book
    
    # def __next__(self):
    #     self.curr_idx += 1
    #     if self.curr_idx <= len(self.book):
    #         return self[self.curr_idx]
    #     else:
    #         raise StopIteration()

    # def reversed_iter(self):
    #     return ReversedBookIterator(self)

    def __enter__(self):
        try:
            self.file = file = open(self.file_name, 'r+')
            # obj = json.load(file)
            self.create_book_from_dict(json.load(file))
            file.seek(0)
        except FileNotFoundError as err:
            pass
        # return file
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):


        if self.file:
            json.dump(self.convert_to_dict_list(), self.file, indent=4)
            print("file wad closed")
            self.file.close()

    
    def show_contacts(self, sort_by=''):
        self._sort(sort_by=sort_by)
        print(str(self))

    # sort_by = property(get_sort_by, set_sort_by, None, "")


if __name__ == '__main__':
    contact = Contact('0230987654', 'Bill', 'Gates', 'New York')
    contact2 = Contact('0230987654', 'Bill', 'Gates')
    # if contact.has_number('0230987654'):  # contact.number == '0230987654' or contact.number2 == 
    #     print("Number already exists")
    # print(contact == contact2)

    BOOK = [
        {"firstname": "Bil", "secondname": "Gates", "number": "38033 9348021", "city": "New York"}, 
        {"firstname": "Mark", "secondname": "Zuckerberg", "number": "38045 9348024"}, 
        {"firstname": "Ilon", "secondname": "Mask", "number": "38077 9348024"},
        {"firstname": "Donald", "secondname": "Trump", "number": "38097 9348024"},
        ]

    # print(contact.__dict__.get('number'))

    book = Book()
    contact5 = Contact('38032 7348021', 'Joe', 'Biden')

    # book.create_book_from_dict(BOOK)
    # book.save_to_json()
    with book:
        book.add_contact(contact5)

    # for cont in book[2::]:  # iter(book) => book.__iter__() => BookIterator(book) [1:3]
    #     print(cont)
    # print(book[:2])
    # print(contact in book)

    # print(book.sort_by)  # book.get_sort_by()
    # book.sort_by = "number"  # ("number",  "secondname")  # book.set_sort_by("number")
    # print(book.sort_by)
    # del book.sort_by
    with book:
        for cont in book:
            print(cont)

    # a = 10
    # print(a)
    # a = a + 10

    # book.show_book(sort_by='number')
    # print()
    # book.show_book(sort_by='firstname')
    # print()
    # book.show_book(sort_by='secondname')

    # print(book)
    # book.book[0]
    # book.book[0] = contact

    # book[1] = contact

    # for cont in book:
    #     print(cont)
    # print(book[1], book[2], sep='\n')
