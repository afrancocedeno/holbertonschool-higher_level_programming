-- creates a table called first_table in the current database
-- create table if already exist not fail.
CREATE TABLE IF NOT EXISTS first_table (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(256));
