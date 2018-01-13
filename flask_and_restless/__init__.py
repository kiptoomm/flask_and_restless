import flask
import flask_restless
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import *

app = flask.Flask(__name__)

# Create our SQLAlchemy DB engine
DATABASE_URI = 'mysql+pymysql://restless_test_admin:restless2018@localhost/restless_test'
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)
s = scoped_session(Session)

Base = declarative_base()
Base.metadata.bind = engine

# Import all models to add them to Base.metadata
from models import Book, Author

Base.metadata.create_all()

manager = flask_restless.APIManager(app, session=s)
# Register flask-restless blueprints to instantiate CRUD endpoints
from controllers import book_api_blueprint, author_api_blueprint

