#task1lesson31.py


"""
Joins

Use the sample SQLite database hr.db (same database you used in the previous lesson for homework tasks)

As a solution to HW, create a file named: task1.sql with all SQL queries:

    write a query in SQL to display the first name, last name, department number, and department name for each employee
    write a query in SQL to display the first and last name, department, city, and state province for each employee
    write a query in SQL to display the first name, last name, department number, and department name, for all employees for departments 80 or 40
    write a query in SQL to display all departments including those where does not have any employee
    write a query in SQL to display the first name of all employees including the first name of their manager
    write a query in SQL to display the job title, full name (first and last name ) of the employee, and the difference between the maximum salary for the job and the salary of the employee
    write a query in SQL to display the job title and the average salary of employees
    write a query in SQL to display the full name (first and last name), and salary of those employees who work in any department located in London
    write a query in SQL to display the department name and the number of employees in each department

"""

from SQLapi import DBQueryHandler

def main():
    
    select_query = DBQueryHandler('hr.db')
    
    print("\n1. Відображення імені, прізвища, номера відділу та назви відділу для кожного співробітника")
    
    # Визначення параметрів для запиту
    table_name = "employees e"
    columns = "e.first_name, e.last_name, e.department_id, d.depart_name"
    join_clause = "JOIN departments d ON e.department_id = d.department_id"
    order_by="d.depart_name"

    # Виконання запиту
    result = select_query.select(table_name, columns, join_clause=join_clause, order_by=order_by)

    # Виведення результату
    for row in result:
        print(row)
        
    print("\n2. Відображення імені, прізвища, відділу, міста та провінції для кожного співробітника")    

    # Визначення параметрів для запиту
    table_name = "employees e"
    columns = "e.first_name, e.last_name, d.depart_name, l.city, l.state_province"
    join_clause = """
    JOIN departments d ON e.department_id = d.department_id
    JOIN locations l ON d.location_id = l.location_id
    """
    order_by = "l.city"

    # Виконання запиту
    result = select_query.select(table_name, columns, join_clause=join_clause, order_by=order_by)

    # Виведення результату
    for row in result:
        print(row)
        
    print("\n3. Відображення імені, прізвища, номера відділу та назви відділу для всіх співробітників у відділах 80 або 40")
    
    # Визначення параметрів для запиту
    table_name = "employees e"
    columns = "e.first_name, e.last_name, e.department_id, d.depart_name"
    join_clause = "JOIN departments d ON e.department_id = d.department_id"
    condition = "e.department_id IN (80, 40)"
    order_by = "e.department_id"

    # Виконання запиту
    result = select_query.select(table_name, columns, condition=condition, order_by=order_by, join_clause=join_clause)

    # Виведення результату
    for row in result:
        print(row)
    
    print("\n4. Відображення всіх відділів, включаючи ті, де немає жодного співробітника")    
    
    # Визначення параметрів для запиту
    table_name = "departments d"
    columns = "d.depart_name, e.first_name, e.last_name"
    join_clause = "LEFT JOIN employees e ON d.department_id = e.department_id"
    order_by = "d.depart_name"

    # Виконання запиту
    result = select_query.select(table_name, columns, join_clause=join_clause, order_by=order_by)

    # Виведення результату
    for row in result:
        print(row)
        
    print("\n5. Відображення імені всіх співробітників, включаючи ім'я їхнього менеджера")   
    
    # Визначення параметрів для запиту
    table_name = "employees e"
    columns = 'e.first_name AS "Employee First Name", m.first_name AS "Manager First Name"'
    join_clause = "LEFT JOIN employees m ON e.manager_id = m.employee_id"
    order_by = "m.first_name"

    # Виконання запиту
    result = select_query.select(table_name, columns, join_clause=join_clause, order_by=order_by)

    # Виведення результату
    for row in result:
        print(row)
        
    print("\n6. Відображення назви посади, повного імені (ім'я та прізвище) співробітника та різниці між максимальною зарплатою для посади та зарплатою співробітника")
    
    # Визначення параметрів для запиту
    table_name = "employees e"
    columns = "j.job_title, e.first_name || ' ' || e.last_name AS 'Full Name', (j.max_salary - e.salary) AS 'Salary Difference'"
    join_clause = "JOIN jobs j ON e.job_id = j.job_id"
    order_by = "j.job_title, e.last_name"

    # Виконання запиту
    result = select_query.select(table_name, columns, join_clause=join_clause, order_by=order_by)

    # Виведення результату
    for row in result:
        print(row)
        
    print("\n7. Відображення назви посади та середньої зарплати співробітників")
    
    # Визначення параметрів для запиту
    table_name = "employees e"
    columns = "j.job_title, AVG(e.salary) AS 'Average Salary'"
    join_clause = "JOIN jobs j ON e.job_id = j.job_id"
    group_by = "j.job_title"

    # Виконання запиту
    result = select_query.select(table_name, columns, join_clause=join_clause, group_by=group_by)

    # Виведення результату
    for row in result:
        print(row)
        
    print("\n8. Відображення повного імені (ім'я та прізвище) та зарплати тих співробітників, які працюють у будь-якому відділі, розташованому в Лондоні")
    
    # Визначення параметрів для запиту
    table_name = "employees e"
    columns = "e.first_name || ' ' || e.last_name AS 'Full Name', e.salary"
    join_clause = """
    JOIN departments d ON e.department_id = d.department_id
    JOIN locations l ON d.location_id = l.location_id
    """
    condition = "l.city = 'London'"
    order_by = "e.last_name"

    # Виконання запиту
    result = select_query.select(table_name, columns, join_clause=join_clause, condition=condition, order_by=order_by)

    # Виведення результату
    for row in result:
        print(row)
        
    print("\n9. Відображення назви відділу та кількості співробітників у кожному відділі")
    
    # Визначення параметрів для запиту
    table_name = "departments d"
    columns = "d.depart_name, COUNT(e.employee_id) AS 'Number of Employees'"
    join_clause = "LEFT JOIN employees e ON d.department_id = e.department_id"
    group_by = "d.depart_name"

    # Виконання запиту
    result = select_query.select(table_name, columns, join_clause=join_clause, group_by=group_by)

    # Виведення результату
    for row in result:
        print(row)
        
    print()
        
    # Закриття з'єднання
    select_query.close()
    
if __name__ == "__main__":
    main()



