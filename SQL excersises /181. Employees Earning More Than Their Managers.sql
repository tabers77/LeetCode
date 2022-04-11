# Write your MySQL query statement below
# IF SALARY OF EMPLOYEE > manager salry return  name 


SELECT

a.name as 'Employee'

from Employee a

# Observe that here I use manager id as the common key 
JOIN Employee b on a.managerId = b.id 

where a.salary > b.salary 
