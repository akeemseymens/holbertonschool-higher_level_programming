-- Display the max temperature in each state
SELECT state, MAX(value) AS Max_Temperature FROM temperatures GROUP BY state ORDER BY state;