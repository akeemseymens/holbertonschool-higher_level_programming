--Script that lists the number of records with same score in the table of database
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY score DESC;