#task2lesson30.py


"""
    Select queries

Use the sample SQLite database hr.db

SQLite database hr.db link:

Link to file

 

As a solution to HW, create a file named: task2.sql with all SQL queries:

    write a query to display the names (first_name, last_name) using alias name "First Name", "Last Name" from the table of employees;
    write a query to get the unique department ID from the employee table
    write a query to get all employee details from the employee table ordered by first name, descending
    write a query to get the names (first_name, last_name), salary, PF of all the employees (PF is calculated as 12% of salary)
    write a query to get the maximum and minimum salary from the employees table
    write a query to get a monthly salary (round 2 decimal places) of each and every employee

"""


from SQLapi import DBDataDefinitionHandler
from SQLapi import DBDataManipulationHandler
from SQLapi import DBQueryHandler

def main():
    select_db = DBQueryHandler('hr.db')
    
    query_result = select_db.select(
        table_name="employees",
        columns='first_name AS "First Name", last_name AS "Last Name"'
    )

    print("Результат запиту:")
    for row in query_result:
        print(row)
        
    # Виконання запиту SELECT DISTINCT з сортуванням
    query_result = select_db.select(
        table_name="employees",
        columns="DISTINCT department_id",
        order_by="department_id"
    )

    # Виведення результатів
    print("\nУнікальні department_id:")
    for row in query_result:
        print(row[0])
        
    # Виконання запиту SELECT з сортуванням за first_name у зворотному порядку
    query_result = select_db.select(
        table_name="employees",
        columns="*",
        order_by="first_name DESC"
    )

    # Виведення результатів
    print("\nСпівробітники, відсортовані за first_name (DESC):")
    for row in query_result:
        print(row)
        
    # Виконання запиту SELECT з обчисленням PF (12% від salary)
    query_result = select_db.select(
        table_name="employees",
        columns="first_name, last_name, salary, (salary * 0.12) AS PF"
    )

    # Виведення результатів
    print("\nСпівробітники з їхніми зарплатами та PF (12% від salary):")
    for row in query_result:
        print(f"Ім'я: {row[0]}, Прізвище: {row[1]}, Зарплата: {row[2]}, PF: {row[3]:.2f}")
        
    # Виконання запиту SELECT для отримання максимальної та мінімальної зарплати
    query_result = select_db.select(
        table_name="employees",
        columns='MAX(salary) AS "Maximum Salary", MIN(salary) AS "Minimum Salary"'
    )

    # Виведення результатів
    max_salary, min_salary = query_result[0]
    print(f"\nМаксимальна зарплата: {max_salary}")
    print(f"\nМінімальна зарплата: {min_salary}")
    
    # Виконання запиту SELECT для отримання місячної зарплати (округленої до 2 десяткових знаків)
    query_result = select_db.select(
        table_name="employees",
        columns="first_name, last_name, ROUND(salary / 12, 2) AS 'Monthly Salary'",
        order_by="last_name"
    )

    # Виведення результатів
    print("\nСпівробітники з їхніми місячними зарплатами:")
    for row in query_result:
        print(f"Ім'я: {row[0]}, Прізвище: {row[1]}, Місячна зарплата: {row[2]:.2f}")
    
    select_db.close()

if __name__ == "__main__":
    main()
