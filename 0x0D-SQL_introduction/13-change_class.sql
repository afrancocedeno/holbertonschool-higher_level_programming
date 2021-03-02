--  script that removes all records with a score <= 5
-- in the table second_table of the database hbtn_0c_0
-- https://www.w3schools.com/sql/sql_delete.asp
-- DELETE FROM table_name WHERE condition;
DELETE FROM second_table WHERE score <= 5;
