# Write your MySQL query statement below
WITH temp AS (
    SELECT
        player_id,
        event_date,
        DATE_ADD(MIN(event_date) OVER (PARTITION BY player_id), INTERVAL 1 DAY) AS second_date
    FROM Activity  
), temp2 AS (
    SELECT DISTINCT player_id
    FROM temp
    WHERE event_date = second_date
)

SELECT ROUND((SELECT COUNT(*) FROM temp2) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction;