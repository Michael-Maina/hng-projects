-- Setup database and user
DROP DATABASE IF EXISTS api_db;

CREATE DATABASE IF NOT EXISTS api_db;

CREATE USER IF NOT EXISTS 'username'@`localhost` IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON `api_db`.* TO 'username'@`localhost`;
FLUSH PRIVILEGES;

USE api_db;