from flask_restful import Resource, Api
from flask_and_restless import models, app

api = Api(app)

class AuthorResource(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(AuthorResource, '/restful/')