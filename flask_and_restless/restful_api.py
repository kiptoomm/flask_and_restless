from flask_restful import Resource, Api
from flask_and_restless import models, app

api = Api(app)

class AuthorAPI(Resource):
    def get(self, author_id):
        return {'hello': 'world' + author_id}

class AuthorAPIList(Resource):
    def get(self):
        return {'hellos': 'world'}

api.add_resource(AuthorAPI, '/restful/authors/<author_id>')
api.add_resource(AuthorAPIList, '/restful/authors/')