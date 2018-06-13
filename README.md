# flask_and_restless
creates basic app based on the tutorial at http://thelaziestprogrammer.com/sharrington/web-development/sqlalchemy-defined-rest-api

## quick setup to test the app locally (on your dev machine)
from project root:

* create and activate a virtual environment with virtualenv or equivalent:

  `virtualenv venv`; `source venv/bin/activate`
        
* install required dependencies into your virtual env
* [Bundle 3rd-party libraries](https://cloud.google.com/appengine/docs/standard/python/tools/using-libraries-python-27) into a folder (usually named 'lib') so that the GAE script `appengine_config.py` can find the dependencies. We have a script to somewhat automate this part:

    `source gae_install_libs.sh`  
* install the [GCP SDK](https://cloud.google.com/appengine/docs/standard/go/download) (`gcloud` tool) if you don't have it set up already
so you can connect to the Google Cloud SQL where the project/database is hosted
* Ensure you're in the right GCP project:

        `gcloud config list`

        ... or switch to the right one with:
        
        `gcloud config set project flask-and-restless`

* run the local server and launch the app as: 

    `dev_appserver app-dev.yaml` 

* You should now be able to access the endpoints such as: `http://localhost:8080/api/author/1/books`

## generating test data
### using filldb.info:
1. `$ python generate_data.py # generates the schema file 'mock_data_schema.sql'` 

upload or copy the contents of the schema file into [filldb](http://filldb.info/dummy/step1)
2. generate the full (or partial) database file (a .sql) and download it
3. connect to the mysql database (CloudSQL) instance:

    `./cloud_sql_proxy -instances=flask-and-restless:europe-west1:flask-restless-db=tcp:3306`
    
4. import data into the mysql database (might re-create tables, remove the drop/create) directives
in the file if you don't want a complete rewrite:

    `mysql -u root -p flask_restless_db < databasefilefromfilldb.sql --host 127.0.0.1`
    
    if you see errors like `RROR 1217 (23000) at line 5: Cannot delete or update a parent row: a foreign key constraint fails`:
    rearrange the order of, or remove, the drop/create statements so foreign key constraints are satisfied

