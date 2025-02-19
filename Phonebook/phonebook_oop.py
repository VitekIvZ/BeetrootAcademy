
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

class Book:
    def __init__(self, contact_list=[], sort_by='secondname'):
        self.book = contact_list
        self.sort_by = sort_by
        if contact_list:
            self._sort()

    def create_book_from_dict(self, book_dict_list): 
        """
        book = [
        {"firstname": "Bil", "secondname": "Gates", "number": "380339348021", "city": "New York"}, 
        {"firstname": "Mark", "secondname": "Zuckerberg", "number": "380459348024"}, 

        ]
        """
        for record in book_dict_list:
            contact = Contact(
                number=record['number'], 
                firstname=record['firstname'], 
                secondname=record['secondname'], 
                city=record['city']
            )
            self.book.append(contact)
        self._sort()

    def add_contact(self, contact):
        self.book.append(contact)
        self._sort()

    def _sort(self, sort_par=''):
        if sort_par:
            pass # use sort_par
        else:
            pass # use self.sort_by

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
        # save book
        pass


if __name__ == '__main__':
    contact = Contact('0230987654', 'Bill', 'Gates', 'New York')

    print(contact)