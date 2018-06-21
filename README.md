# flask_and_restless
creates basic app based on the tutorial at http://thelaziestprogrammer.com/sharrington/web-development/sqlalchemy-defined-rest-api

## quick setup with vagrant
This setup is adapted from the [vagrant-gcloud](https://github.com/laander/vagrant-gcloud) project

Ideally, you should still work in a virtual env to isolate dependencies specific to this project from the rest of your machine's

1. install [vagrant](https://www.vagrantup.com/docs/installation/) and [virtualbox](https://www.virtualbox.org/wiki/Downloads)
2. clone this repo and `cd` to the project root
3. provision the ubuntu VM with vagrant (configured from `Vagrantfile` in the root directory):

    `vagrant up`
    
4. enter into the VM with SSH:

    `vagrant ssh`
    
    * Authenticate the gcloud CLI to your google account

        `gcloud auth login`

    * Define the GAE project name for the gcloud utility to use (as set up in Google Console)

        `gcloud config set project 'your-project-name'`
        
    * you might need to manually cd into the [synced folder](https://www.vagrantup.com/docs/synced-folders/) (usually /vagrant), where the project files will be located on the guest machine: `cd /vagrant`
    * the machine should be ready to use, with all the required dependencies installed. proceed with the rest of the operations that you need to run. for example, run the app locally in the VM, you do so as you would in your host machine:
    
    `dev_appserver app-dev.yaml`
    
    assuming you have already started the CloudSQL proxy client (installed in vagrant's home directory):
    
    `~/cloud_sql_proxy -instances=<project instance name>=tcp:3306`
    
    If you encounter an error like `google: could not find default credentials. See https://developers.google.com/accounts/docs/application-default-credentials for more information.`, you might have to set app default credentials first:
    
    `gcloud auth application-default login`
    

## manual setup to test the app locally (on your dev machine)
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

