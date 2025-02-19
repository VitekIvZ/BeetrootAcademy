-- task1.sql

-- 1. Відображення імені, прізвища, номера відділу та назви відділу для кожного співробітника
SELECT e.first_name, e.last_name, e.department_id, d.depart_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id
ORDER BY d.depart_name;

-- 2. Відображення імені, прізвища, відділу, міста та провінції для кожного співробітника
SELECT e.first_name, e.last_name, d.depart_name, l.city, l.state_province
FROM employees e
JOIN departments d ON e.department_id = d.department_id
JOIN locations l ON d.location_id = l.location_id
ORDER BY l.city;

-- 3. Відображення імені, прізвища, номера відділу та назви відділу для всіх співробітників у відділах 80 або 40
SELECT e.first_name, e.last_name, e.department_id, d.depart_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id
WHERE e.department_id IN (80, 40)
ORDER BY e.department_id;

-- 4. Відображення всіх відділів, включаючи ті, де немає жодного співробітника
SELECT d.depart_name, e.first_name, e.last_name
FROM departments d
LEFT JOIN employees e ON d.department_id = e.department_id
ORDER BY d.depart_name;

-- 5. Відображення імені всіх співробітників, включаючи ім'я їхнього менеджера
SELECT e.first_name AS "Employee First Name", m.first_name AS "Manager First Name"
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.employee_id
ORDER BY m.first_name;

-- 6. Відображення назви посади, повного імені (ім'я та прізвище) співробітника та різниці між максимальною зарплатою для посади та зарплатою співробітника
SELECT j.job_title, e.first_name || ' ' || e.last_name AS "Full Name", (j.max_salary - e.salary) AS "Salary Difference"
FROM employees e
JOIN jobs j ON e.job_id = j.job_id
ORDER BY j.job_title, e.last_name;

-- 7. Відображення назви посади та середньої зарплати співробітників
SELECT j.job_title, AVG(DISTINCT e.salary) AS "Average Salary"
FROM employees e
JOIN jobs j ON e.job_id = j.job_id
GROUP BY j.job_title;

-- 8. Відображення повного імені (ім'я та прізвище) та зарплати тих співробітників, які працюють у будь-якому відділі, розташованому в Лондоні
SELECT e.first_name || ' ' || e.last_name AS "Full Name", e.salary
FROM employees e
JOIN departments d ON e.department_id = d.department_id
JOIN locations l ON d.location_id = l.location_id
WHERE l.city = 'London'
ORDER BY e.last_name;

-- 9. Відображення назви відділу та кількості співробітників у кожному відділі
SELECT d.depart_name, COUNT(e.employee_id) AS "Number of Employees"
FROM departments d
LEFT JOIN employees e ON d.department_id = e.department_id
GROUP BY d.depart_name;
