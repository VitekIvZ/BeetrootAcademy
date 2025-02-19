import sqlite3


class DBDataDefinitionHandler:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def create_table(self, table_name, columns):
        """
        Створення таблиці з вказаними стовпцями.
        :table_name: Назва таблиці
        :columns: Словник з назвами стовпців та їх типами даних
        """
        columns_with_types = ', '.join([f"{col} {dtype}" for col, dtype in columns.items()])
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_with_types})"
        self.cursor.execute(query)
        self.connection.commit()
        return f"Table '{table_name}' created successfully."

    def drop_table(self, table_name):
        """
        Видалення таблиці.
        :table_name: Назва таблиці
        """
        query = f"DROP TABLE IF EXISTS {table_name}"
        self.cursor.execute(query)
        self.connection.commit()
        return f"Table '{table_name}' dropped successfully."

    def alter_table_add_column(self, table_name, column_name, column_type):
        """
        Додавання нового стовпця до існуючої таблиці.
        :table_name: Назва таблиці
        :column_name: Назва нового стовпця
        :column_type: Тип даних нового стовпця
        """
        query = f"ALTER TABLE {table_name} ADD COLUMN {column_name} {column_type}"
        self.cursor.execute(query)
        self.connection.commit()
        return f"Column '{column_name}' added to table '{table_name}' successfully."

    def rename_table(self, old_table_name, new_table_name):
        """
        Перейменування таблиці.
        :old_table_name: Поточна назва таблиці
        :new_table_name: Нова назва таблиці
        """
        query = f"ALTER TABLE {old_table_name} RENAME TO {new_table_name}"
        self.cursor.execute(query)
        self.connection.commit()
        return f"Table '{old_table_name}' renamed to '{new_table_name}' successfully."

    def truncate_table(self, table_name):
        """
        Очищення таблиці (видалення всіх даних).
        :table_name: Назва таблиці
        """
        query = f"DELETE FROM {table_name}"
        self.cursor.execute(query)
        self.connection.commit()
        return f"Table '{table_name}' truncated successfully."

    def close(self):
        """
        Закриття з'єднання з базою даних.
        """
        self.connection.close()
        

class DBDataManipulationHandler:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def insert(self, table_name, data):
        """
        Вставка даних у таблицю.
        :table_name: Назва таблиці
        :data: Словник з даними для вставки (ключі - назви стовпців, значення - дані)
        """
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['?'] * len(data))
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        self.cursor.execute(query, tuple(data.values()))
        self.connection.commit()

    def update(self, table_name, set_data, condition):
        """
        Оновлення даних у таблиці.
        :table_name: Назва таблиці
        :set_data: Словник з даними для оновлення (ключі - назви стовпців, значення - нові дані)
        :condition: Умова для оновлення (наприклад, "id = 1")
        """
        set_clause = ', '.join([f"{col} = ?" for col in set_data.keys()])
        query = f"UPDATE {table_name} SET {set_clause} WHERE {condition}"
        self.cursor.execute(query, tuple(set_data.values()))
        self.connection.commit()

    def delete(self, table_name, condition):
        """
        Видалення даних з таблиці.
        :table_name: Назва таблиці
        :condition: Умова для видалення (наприклад, "id = 1")
        """
        query = f"DELETE FROM {table_name} WHERE {condition}"
        self.cursor.execute(query)
        self.connection.commit()

    def close(self):
        """
        Закриття з'єднання з базою даних.
        """
        self.connection.close()

class DBQueryHandler:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def select(self, table_name, columns="*", condition=None, order_by=None):
        """
        Вибірка даних з таблиці.
        :table_name: Назва таблиці
        :columns: Список стовпців для вибірки (за замовчуванням "*" - всі стовпці)
        :condition: Умова для вибірки (наприклад, "id = 1")
        :orrder_by: Стовпець для сортування (наприклад, "department_id")
        :return: Результат вибірки
        """
        query = f"SELECT {columns} FROM {table_name}"
        if condition:
            query += f" WHERE {condition}"
        if order_by:
            query += f" ORDER BY {order_by}"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close(self):
        """
        Закриття з'єднання з базою даних.
        """
        self.connection.close()


def main():
    
    db = DBDataDefinitionHandler('example.db')

    # Створення таблиці
    print(db.create_table('users', {'id': 'INTEGER PRIMARY KEY', 'name': 'TEXT', 'age': 'INTEGER'}))

    # Додавання нового стовпця
    print(db.alter_table_add_column('users', 'email', 'TEXT'))

    manipul_db = DBDataManipulationHandler('example.db')

    # Вставка даних
    manipul_db.insert('users', {'name': 'John Doe', 'age': 30})
    manipul_db.insert('users', {'name': 'Jane Doe', 'age': 25})

    # Оновлення даних
    manipul_db.update('users', {'age': 31}, "name = 'John Doe'")

    # Видалення даних
    manipul_db.delete('users', "name = 'Jane Doe'")

    # Вибірка даних
    select_query = DBQueryHandler('example.db')
    users = select_query.select('users')
    print("Users:", users)

    # Вибірка даних з умовою
    user = select_query.select('users', condition="name = 'John Doe'")
    print("User John Doe:", user)
    
    # Перейменування таблиці
    print(db.rename_table('users', 'clients'))

    # Очищення таблиці
    print(db.truncate_table('clients'))

    # Видалення таблиці
    print(db.drop_table('clients'))

    # Закриття з'єднання
    db.close()
    manipul_db.close()
    select_query.close()


if __name__ == "__main__":
    main()
    