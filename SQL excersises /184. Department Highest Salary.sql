# Write your MySQL query statement below
SELECT
d.name as 'Department',
e.name  as 'Employee',
e.salary as 'Salary'

FROM Employee e JOIN Department d ON e.departmentId = d.id

# Here I select  the maximum salaries per id and choose only those salaries and departaments 
WHERE(e.departmentId, salary ) 
IN 
(SELECT departmentId , MAX(salary) from Employee GROUP BY departmentId )