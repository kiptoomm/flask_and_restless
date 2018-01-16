from marshmallow_jsonapi import  Schema, fields
from flask_restless import DefaultSerializer, DefaultDeserializer
from marshmallow_enum import EnumField
from marshmallow import post_load
from models import Gender, Author, BaseModel


class BaseSchema(Schema):
    id = fields.Integer(dump_only=True)

    class Meta:
        model = BaseModel
        strict = True

    @post_load
    def make_object(self, data):
        return self.Meta.model(**data)

class AuthorSchema(BaseSchema):
    first_name = fields.Str()
    last_name = fields.Str()
    gender = EnumField(Gender)

    class Meta(BaseSchema.Meta):
        type_ = 'author'
        model = Author

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