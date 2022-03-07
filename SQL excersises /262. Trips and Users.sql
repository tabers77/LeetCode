
SELECT
request_at AS 'Day',
ROUND(SUM(IF(status != 'completed',1,0)) / COUNT(status), 2) AS 'Cancellation Rate'


FROM Trips LEFT JOIN Users ON Trips.id = Users.users_id

WHERE request_at BETWEEN "2013-10-01" AND "2013-10-03"
AND client_id IN (SELECT USERS_ID FROM Users WHERE banned = 'No'  )
AND driver_id IN (SELECT USERS_ID FROM Users WHERE banned = 'No'  )

GROUP BY request_at
