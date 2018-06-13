import flask
from flask_restless import APIManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = flask.Flask(__name__)

# DATABASE_URI = 'mysql+pymysql://restless_test_admin:restless2018@localhost/restless_test'
# app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI

from config import app_config

# load runtime variables from config files
app.config.from_pyfile('../config.py')
app.config.from_object(app_config['development']) # todo pass in app config name or env var

db.init_app(app)

from models import Book, Author

manager = APIManager(app, session=db.session)
# Register flask-restless blueprints to instantiate CRUD endpoints
from controllers import book_api_blueprint, author_api_blueprint


