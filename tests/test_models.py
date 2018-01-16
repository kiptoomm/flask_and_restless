import unittest
from flask_testing import TestCase
from flask_and_restless import app, db
from flask_and_restless.models import Author, Book, Gender
from flask_and_restless.schemas import AuthorSchema

class TestBase(TestCase):

    def create_app(self):
        _app = app
        return _app

    def setUp(self):
        db.drop_all()
        db.create_all()

        author = Author(first_name='first1', last_name='last1')
        book = Book(title='title1', author_id=author.id, is_available=True)

        db.session.add(author)
        db.session.add(book)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        #db.drop_all()

class TestModels(TestBase):

    def test_author(self):
        author = db.session.query(Author).get(1)
        self.assertEqual(author.first_name, 'first1')

    def test_author_schema(self):
        author = Author(first_name='abc', last_name='xyz', gender=Gender.MALE)
        schema = AuthorSchema()
        data, errors = schema.dump(author)
        print data, errors


if __name__ == '__main__':
    unittest.main()