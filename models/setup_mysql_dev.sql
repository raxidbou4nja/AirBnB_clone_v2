-- create or use the database "hbnb_dev_db"
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;


-- greate or use the user "hbnb_dev"
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';


-- grant privileges to "hbnb_dev" on DataBase "hbnb_dev_db"
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';


-- grant SELECT privilege on performance_schema to "hbnb_dev"
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
