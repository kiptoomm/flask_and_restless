from marshmallow_jsonapi import  Schema, fields
from flask_restless import DefaultSerializer, DefaultDeserializer
from marshmallow_enum import EnumField
from marshmallow import post_load
from models import Gender, Author, BaseModel, Book


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
    created_at = fields.DateTime()
    updated_at = fields.DateTime()

    class Meta(BaseSchema.Meta):
        type_ = 'author'
        model = Author

class BookSchema(BaseSchema):
    title = fields.Str()
    author_id = fields.Int()
    is_available = fields.Boolean()
    author = fields.Nested('flask_and_restless.schemas.AuthorSchema', many=False)

    class Meta(BaseSchema.Meta):
        type_ = 'book'
        model = Book



class MarshmallowSerializer(DefaultSerializer):

    schema_class = None

    def serialize(self, instance, only=None):
        schema = self.schema_class(only=only)
        return schema.dump(instance).data

    def serialize_many(self, instances, only=None):
        schema = self.schema_class(many=True, only=only)
        return schema.dump(instances).data


class MarshmallowDeserializer(DefaultDeserializer):

    schema_class = None

    def deserialize(self, document):
        schema = self.schema_class()
        return schema.load(document).data

    def deserialize_many(self, document):
        schema = self.schema_class(many=True)
        return schema.load(document).data

class AuthorSerializer(MarshmallowSerializer):
    schema_class = AuthorSchema

class AuthorDeserializer(MarshmallowDeserializer):
    schema_class = AuthorSchema

class BookSerializer(MarshmallowSerializer):
    schema_class = BookSchema

class BookDeserializer(MarshmallowDeserializer):
    schema_class = BookSchema