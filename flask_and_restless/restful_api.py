from flask_restful import Resource, Api, fields, marshal
from flask_and_restless import models, app, schemas

api = Api(app)

author_fields = {
    'id': fields.Integer,
    'first_name': fields.String,
    'last_name': fields.String
}

class AuthorAPI(Resource):
    def get(self, author_id):
        author = models.Author.query.get(author_id)
        author_serializer = schemas.AuthorSerializer()
        return author_serializer.serialize(author)

class AuthorAPIList(Resource):
    def get(self):
        authors = models.Author.query.all()
        author_serializer = schemas.AuthorSerializer()
        return author_serializer.serialize_many(authors)

api.add_resource(AuthorAPI, '/restful/authors/<author_id>')
api.add_resource(AuthorAPIList, '/restful/authors/')