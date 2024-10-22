-- comment
USE hbtn_0c_0

SELECT score, 
    COUNT(*) AS number
FROM second_table
GROUP BY score
GROUP BY score DESC;
