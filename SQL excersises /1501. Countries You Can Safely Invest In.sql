SELECT

country

FROM

(
SELECT
c.name AS country,

AVG(b.duration) AVG_DURATION , 

(SELECT AVG(duration)  FROM  Calls) AS GLOBAL_AVG_DURATION

FROM Person a  
JOIN Calls b ON a.id = b.caller_id OR a.id = b.callee_id
JOIN Country c ON LEFT (phone_number, 3 ) = c.country_code

GROUP BY c.name
) T1


WHERE AVG_DURATION > GLOBAL_AVG_DURATION

