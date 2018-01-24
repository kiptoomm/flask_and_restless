from flask_restful import Resource, Api, fields, marshal
from flask_and_restless import models, app

api = Api(app)

author_fields = {
    'id': fields.Integer,
    'first_name': fields.String,
    'last_name': fields.String
}

class AuthorAPI(Resource):
    def get(self, author_id):
        author = models.Author.query.get(author_id)
        print 'author: ', author
        return {'author': marshal(author, author_fields)}

class AuthorAPIList(Resource):
    def get(self):
        authors = models.Author.query.all()
        print 'authors: ', authors
        return {'author': marshal(authors, author_fields)}

api.add_resource(AuthorAPI, '/restful/authors/<author_id>')
api.add_resource(AuthorAPIList, '/restful/authors/')