# Write your MySQL query statement below


SELECT
# IF SALARY OF EMPLOYEE > mangaer salry return  name 

a.name as 'Employee'

from Employee a
JOIN Employee b on a.managerId = b.id 

where a.salary > b.salary 
