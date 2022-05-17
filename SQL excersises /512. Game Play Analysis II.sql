# Solution 1
SELECT
a.player_id,
b.device_id
FROM
(SELECT
player_id,
MIN(event_date) AS event_date
FROM Activity GROUP BY player_id) a 

JOIN Activity b 
ON a.player_id = b.player_id 
# OBS: In order to choose only min dates we join on that key 
AND a.event_date = b.event_date

# Solution 2 
select 
a.player_id,
a.device_id
from 
Activity a inner join 

(select player_id, min(event_date) as event_date from Activity group by player_id  ) b 
on a.event_date = b.event_date and  a.player_id = b.player_id