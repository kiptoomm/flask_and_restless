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


