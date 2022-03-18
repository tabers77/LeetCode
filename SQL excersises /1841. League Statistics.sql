# Write your MySQL query statement below

SELECT
team_name,
COUNT(home_team_id) as matches_played, 

SUM(CASE 
WHEN home_team_goals > away_team_goals THEN 3 
WHEN home_team_goals = away_team_goals THEN 1
ELSE 0 END) as points,

SUM(home_team_goals) AS goal_for , 
SUM(away_team_goals) AS goal_against,
SUM(home_team_goals) - SUM(away_team_goals)  AS goal_diff


FROM 
# Normalize table equalizing ids so home_team_id == away_team_id and home_team_goals == away_team_goals
(SELECT home_team_id , home_team_goals, away_team_goals 
FROM matches
UNION ALL
SELECT away_team_id as home_team_id, away_team_goals as home_team_goals, home_team_goals as away_team_goals 
FROM matches) a
JOIN Teams b ON a.home_team_id = b.team_id

GROUP BY team_name

order by 3 desc, 6 desc, 1



