-- task2.sql

-- Запит для відображення імен (first_name, last_name) з використанням псевдонімів "First Name", "Last Name"
SELECT first_name AS "First Name", last_name AS "Last Name"
FROM employees;

-- Запит для отримання унікальних ID відділів з таблиці employee, відсортованих за зростанням
SELECT DISTINCT department_id
FROM employees
ORDER BY department_id;

-- Запит для отримання всіх деталей співробітників з таблиці employee, відсортованих за ім'ям у порядку спадання
SELECT *
FROM employees
ORDER BY first_name DESC;

-- Запит для отримання імен (first_name, last_name), зарплати, PF всіх співробітників (PF розраховується як 12% від зарплати)
SELECT first_name, last_name, salary, (salary * 0.12) AS PF
FROM employees;

-- Запит для отримання максимальної та мінімальної зарплати з таблиці employees
SELECT MAX(salary) AS "Maximum Salary", MIN(salary) AS "Minimum Salary"
FROM employees;

-- Запит для отримання місячної зарплати (округленої до 2 десяткових знаків) кожного співробітника
SELECT first_name, last_name, ROUND(salary / 12, 2) AS "Monthly Salary"
FROM employees
ORDER BY last_name;