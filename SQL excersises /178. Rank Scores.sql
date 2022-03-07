# Write your MySQL query statement below

# Solution 1 
SELECT 

s1.Score, 
(SELECT COUNT(DISTINCT Score) from Scores s2 WHERE s2.Score >= s1.Score  ) as 'rank'

FROM Scores s1
order by s1.Score DESC

# Solution 2
select S.Score, Dense_Rank() over(order by S.Score desc) 'Rank' from Scores S
