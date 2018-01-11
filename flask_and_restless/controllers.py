from flask_and_restless import app, s, manager
from flask_and_restless.models\
    import Book, Author
from schemas import AuthorSerializer, AuthorDeserializer

author_api_blueprint = manager.create_api(Author,
        methods=['GET', 'PATCH', 'POST', 'DELETE'],
        serializer_class=AuthorSerializer,
        deserializer_class=AuthorDeserializer)
book_api_blueprint = manager.create_api(Book,
        methods=['GET', 'PATCH', 'POST', 'DELETE'])

