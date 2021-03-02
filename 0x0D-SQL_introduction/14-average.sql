-- script that computes the score average of all records
-- in the table second_table of the database hbtn_0c_0
-- https://www.w3schools.com/sql/sql_count_avg_sum.asp
-- SELECT AVG(column_name)
-- FROM table_name
-- WHERE condition;
SELECT AVG(score) AS average
FROM second_table
