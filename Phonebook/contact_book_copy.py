"""
book = {"38033934802": {"firstname": "Bil", "secondname": "Gates"}}
        "fullname": {}

book = [
        {"firstname": "Bil", "secondname": "Gates", "number": "380339348021", "city": "New York"}, 
        {"firstname": "Mark", "secondname": "Zuckerberg", "number": "380459348024"}, 

    ]


1. write to file  +
2. read from file +
3. add new entry
4. delete record
5. search by ...

8. update number
9. print book     +

"""
import json


def save_to_file(func):
    def wrapper(book, *args, file_name='book.json', **kwargs):
        file = open(file_name, 'w')
        result = func(file, book, *args, **kwargs)
        file.close()
        return result
    return 


def write_book(obj, file_name='book.json'):
    """
    
    """
    with open(file_name, 'w') as fp:
        json.dump(obj, fp, indent=4)


def read_book(file_name='book.json'):
    """
    
    """
    with open(file_name, 'r') as fp:
        obj = json.load(fp)
    return obj


@save_to_file
def add_record(file, book, firstname='', secondname='', number='', city=""):
    """
    
    """
    rec = {"firstname": firstname, 
           "secondname": secondname, 
           "number": number, 
           "city": city}
    
    book.append(rec)
    json.dump(book, file, indent=4)
    return book


@save_to_file
def remove_contact(file, book, number):
    # idx = ...
    # del book[idx]
    pass


def search_by(book, by='number'):
    """
    
    """
    contact = None
    return contact


def test():


    pass


if __name__ == '__main__':
    # book = [
         
    #     {"firstname": "Mark", "secondname": "Zuckerberg", "number": "380459348024", "city": "New York"}, 
    #     {"firstname": "Bil", "secondname": "Gates", "number": "380539348021", "city": "New York"},
    # ]
    # print_book(book)
    # write_book(book)
    # book = read_book()
    # print_book(sorted(book, key=lambda rec: rec['number']))
    # print_book(book, sort_by='number')
    # add_record(book, firstname='', secondname='', number='')
    test()