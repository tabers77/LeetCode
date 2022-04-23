SELECT
DISTINCT a.num as "ConsecutiveNums"
FROM Logs a
# This will generate difrent ids but the same number since we will increment the id keeping the same number
JOIN Logs b ON a.id = b.id + 1 AND a.num = b.num 
JOIN Logs c ON a.id = c.id + 2 AND a.num =c.num 