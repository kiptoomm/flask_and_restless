# flask_and_restless
creates basic app following tutorial on http://thelaziestprogrammer.com/sharrington/web-development/sqlalchemy-defined-rest-api

## requirements
from project root:

`pip install -r requirements.txt`

*note*: you may run into trouble installing the flask-restless dependency. We had to use the dev version of the library as the latest features are not in a public release yet. So you might have to install it directly from source (remove the flask-restless entry from requirements.txt first):

`pip install git+https://github.com/jfinkels/flask-restless.git`

## database setup
relies on mysql+pymsql driver (installation on your local machine is assumed). 
run these commands to create the database:

`CREATE DATABASE restless_test;`

`CREATE USER 'restless_test_admin'@'localhost' IDENTIFIED BY 'restless2018';`

`GRANT ALL PRIVILEGES ON restless_test . * TO 'restless_test_admin'@'localhost';`


## from project root, run as: 
`$ python run.py` 

