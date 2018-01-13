# flask_and_restless
creates basic app following tutorial on http://thelaziestprogrammer.com/sharrington/web-development/sqlalchemy-defined-rest-api

## database setup
relies on mysql+pymsql driver (installation on your local machine is assumed). 
run these commands to create the database:

`CREATE DATABASE restless_test;`

`CREATE USER 'restless_test_admin'@'localhost' IDENTIFIED BY 'restless2018';`

`GRANT ALL PRIVILEGES ON restless_test . * TO 'restless_test_admin'@'localhost';`


## from project root, run as: 
`$ python run.py` 

