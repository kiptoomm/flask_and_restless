from flask_and_restless import app, s, manager
from flask_and_restless.models\
    import Book, Author

author_api_blueprint = manager.create_api(Author,
        methods=['GET', 'PATCH', 'POST', 'DELETE'])
book_api_blueprint = manager.create_api(Book,
        methods=['GET', 'PATCH', 'POST', 'DELETE'])

