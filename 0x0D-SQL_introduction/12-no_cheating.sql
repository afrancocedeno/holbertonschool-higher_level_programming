-- script that updates the score of Bob to 10 in the table second_table.
-- https://www.w3schools.com/sql/sql_update.asp
-- UPDATE table_name
-- SET column1 = value1, column2 = value2, ...
-- WHERE condition;
UPDATE second_table
set score = 10
WHERE name = 'Bob';
