# Write your MySQL query statement below
SELECT
email AS 'Email'

FROM Person
GROUP BY email

HAVING COUNT(email) > 1 

# Solution 2  
select
email
from
(
select
email, 
count(*) count_

from Person 
group by email
having count_ > 1 
    ) c