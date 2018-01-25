from flask_restful import Resource, Api, fields, marshal, reqparse
from flask_and_restless import models, app, schemas, db
from flask import request

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

    def patch(self, author_id):
        author = models.Author.query.get(author_id)
        author_schema = schemas.AuthorSchema()
        args = request.get_json()
        author_s, errors = author_schema.load(args)
        print 'deserialized, type: , errors: ', author_s.__dict__, type(author_s), errors

        for k, v in author_s.__dict__.iteritems():
            print 'k = {}, v = {}'.format(k, v)
            if v != None:
                setattr(author, k, v)
        db.session.commit()
        #return author_serializer.serialize(author)

class AuthorAPIList(Resource):
    def get(self):
        authors = models.Author.query.all()
        author_serializer = schemas.AuthorSerializer()
        return author_serializer.serialize_many(authors)

api.add_resource(AuthorAPI, '/restful/authors/<author_id>')
api.add_resource(AuthorAPIList, '/restful/authors/')