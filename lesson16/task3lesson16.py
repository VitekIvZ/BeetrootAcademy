#task3lesson16.py


"""
    Product Store

Write a class Product that has three attributes:

    type
    name
    price

Then create a class ProductStore, which will have some Products and will operate with all products 
in the store. All methods, in case they can't perform its action, should raise ValueError with 
appropriate error information.

Tips: Use aggregation/composition concepts while implementing the ProductStore class. 
You can also implement additional classes to operate on a certain type of product, etc.

Also, the ProductStore class must have the following methods:

    add(product, amount) - adds a specified quantity of a single product with a predefined price premium for your store(30 percent)
    set_discount(identifier, percent, identifier_type='name') - adds a discount for all products specified by input identifiers (type or name). The discount must be specified in percentage
    sell_product(product_name, amount) - removes a particular amount of products from the store if available, in other case raises an error. It also increments income if the sell_product method succeeds.
    get_income() - returns amount of many earned by ProductStore instance.
    get_all_products() - returns information about all available products in the store.
    get_product_info(product_name) - returns a tuple with product name and amount of items in the store.

'''

class Product:

    pass

class ProductStore:

pass

p = Product('Sport', 'Football T-Shirt', 100)

p2 = Product('Food', 'Ramen', 1.5)

s = ProductStore()

s.add(p, 10)

s.add(p2, 300)

s.sell_product('Ramen', 10)

assert s.get_product_info('Ramen') == ('Ramen', 290)

'''
"""

class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price

class ProductStore:
    def __init__(self):
        self.products = {}
        self.income = 0

    def add(self, product, amount):
        if product.name in self.products:
            self.products[product.name]['amount'] += amount
        else:
            self.products[product.name] = {
                'product': product,
                'amount': amount,
                'price': product.price * 1.3  # Додаємо 30% до ціни продукту
            }

    def set_discount(self, identifier, percent, identifier_type='name'):
        if identifier_type == 'name':
            if identifier in self.products:
                self.products[identifier]['price'] *= (1 - percent / 100)
            else:
                raise ValueError(f"Product with name '{identifier}' not found.")
        elif identifier_type == 'type':
            found = False
            for product_info in self.products.values():
                if product_info['product'].type == identifier:
                    product_info['price'] *= (1 - percent / 100)
                    found = True
            if not found:
                raise ValueError(f"Product with type '{identifier}' not found.")
        else:
            raise ValueError("Invalid identifier type. Use 'name' or 'type'.")

    def sell_product(self, product_name, amount):
        if product_name in self.products:
            if self.products[product_name]['amount'] >= amount:
                self.products[product_name]['amount'] -= amount
                self.income += self.products[product_name]['price'] * amount
            else:
                raise ValueError(f"Not enough '{product_name}' in stock.")
        else:
            raise ValueError(f"Product '{product_name}' not found.")

    def get_income(self):
        return self.income

    def get_all_products(self):
        return [(product_info['product'].name, product_info['amount']) for product_info in self.products.values()]

    def get_product_info(self, product_name):
        if product_name in self.products:
            return (product_name, self.products[product_name]['amount'])
        else:
            raise ValueError(f"Product '{product_name}' not found.")


def test():
    p = Product('Sport', 'Football T-Shirt', 100)
    p2 = Product('Food', 'Ramen', 1.5)

    s = ProductStore()

    s.add(p, 10)
    s.add(p2, 300)

    s.sell_product('Ramen', 10)

    assert s.get_product_info('Ramen') == ('Ramen', 290)
    
    return "All assertions passed."

if __name__ == "__main__":
    
    print(test())
    
