

CREATE DATABASE IF NOT EXISTS madb;
CREATE USER IF NOT EXISTS 'dba'@'%' IDENTIFIED BY 'Password123$';

GRANT ALL PRIVILEGES ON madb.* TO 'dba'@'%' BY 'Password123$';
GRANT ALL PRIVILEGES ON *.* TO 'dba'@'localhost' IDENTIFIED BY 'Password123$';

FLUSH PRIVILEGES;

CREATE TABLE users ( id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), email VARCHAR(100) );
INSERT INTO users (name, email) VALUES ('ali', 'ali@example.com');
INSERT INTO users (name, email) VALUES ('haldun', 'haldun@techniaa.com');
USE madb ; 

-- Debugging lines
SELECT User, Host FROM mysql.user;
SHOW GRANTS FOR 'dba'@'%';
