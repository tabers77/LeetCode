SELECT
    d.Name AS 'Department', e1.Name AS 'Employee', e1.Salary
FROM
    Employee e1
        JOIN
    Department d ON e1.DepartmentId = d.Id
WHERE
    3 > (SELECT
            COUNT(DISTINCT e2.Salary)
        FROM
            Employee e2
        WHERE
            e2.Salary > e1.Salary
                AND e1.DepartmentId = e2.DepartmentId
        )
;


# Solution 2 
select d.Name as Department, a.Name as Employee, a.Salary 
from (

# 1 Create a ranking by departament id and order by salary to obtain rank per top salary 
select e.*, dense_rank() over (partition by DepartmentId order by Salary desc) as DeptPayRank 
from Employee e 
) a 

join Department d
on a. DepartmentId = d. Id 

# 2 Choose only the top 3 
where DeptPayRank <=3; 