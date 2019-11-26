--Display the max temperature in each state
SELECT state, MAX(value) AS Max_Temperature FROM temperature GROUP BY state ORDER BY state;