from marshmallow_jsonapi import  Schema, fields
from flask_restless import DefaultSerializer, DefaultDeserializer

class AuthorSchema(Schema):
    id = fields.Str(dump_only=True)
    first_name = fields.Str()
    last_name = fields.Str()

    class Meta:
        type_ = 'author'
        strict = True

class AuthorSerializer(DefaultSerializer):
    def serialize(self, instance, only=None):
        author_schema = AuthorSchema(only=only)
        return author_schema.dump(instance).data

    def serialize_many(self, instances, only=None):
        uthor_schema = AuthorSchema(many=True, only=only)
        return uthor_schema.dump(instances).data

class AuthorDeserializer(DefaultDeserializer):
    def serialize(self, instance, only=None):
        author_schema = AuthorSchema(only=only)
        return author_schema.load(instance).data

    def serialize_many(self, instances, only=None):
        author_schema = AuthorSchema(many=True, only=only)
        return author_schema.load(instances).data