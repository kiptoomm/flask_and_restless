'''
    populates the development database with debug data
'''
from flask_and_restless import db, app

def create_empty_tables():
    app.app_context().push()
    db.drop_all()
    db.create_all()

if __name__ == '__main__':
    print 'running database table creator'

    create_empty_tables()

