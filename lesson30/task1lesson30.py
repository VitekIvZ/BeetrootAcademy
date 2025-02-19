#task1lesson30.py


"""
    Create a table

Create a table of your choice inside the sample SQLite database, rename it, and add a new column. 
Insert a couple rows inside your table. Also, perform UPDATE and DELETE statements on inserted rows.

As a solution to this task, create a file named: task1.sql, with all the SQL statements you have used 
to accomplish this task
"""

#import sqlite3
from SQLapi import DBDataDefinitionHandler
from SQLapi import DBDataManipulationHandler
from SQLapi import DBQueryHandler

def main():
    
    db = DBDataDefinitionHandler('lesson30.db')

    # Створення таблиці
    print(db.create_table('users', {'id': 'INTEGER PRIMARY KEY', 'name': 'TEXT', 'city': 'TEXT', 'phone_number':'INTEGER'}))

    # Перейменування таблиці
    print(db.rename_table('users', 'clients'))
    
    # Додавання нового стовпця
    print(db.alter_table_add_column('clients', 'email', 'TEXT'))
    
    oper_db = DBDataManipulationHandler('lesson30.db')
    
    # Вставка даних
    oper_db.insert('clients', {'name': 'Bret Peet', 'city': 'Mexico', 'phone_number': '123456789', 'email':'bp@exp.com'})
    oper_db.insert('clients', {'name': 'Jhon Deer', 'city': 'Ottava', 'phone_number': '987654321', 'email':'jd@exp.com'})
    oper_db.insert('clients', {'name': 'Omar Green', 'city': 'Tokio', 'phone_number': '678912345', 'email':'og@exp.com'})
    
    # Вибірка даних
    select_query = DBQueryHandler('lesson30.db')
    users = select_query.select('clients')
    print("Clients:", users)
    
    # Оновлення даних
    oper_db.update('clients', {'city': 'Berlin', 'phone_number': '432156789'}, "id = 1")
    users = select_query.select('clients')
    print("Clients after update:", users)

    # Видалення даних
    oper_db.delete('clients', "name = 'Bret Peet'")
    users = select_query.select('clients')
    print("Clients after delete rows:", users)
        
    # Закриття з'єднання
    db.close()
    oper_db.close()
    select_query.close()
    
if __name__ == "__main__":
    main()
