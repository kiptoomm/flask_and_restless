import unittest
from flask_testing import TestCase
from flask_and_restless.models import Author, Book, Gender
from flask_and_restless import Base, s, app

class TestBase(TestCase):

    def create_app(self):
        _app = app
        return _app

    def setUp(self):
        Base.metadata.drop_all()
        Base.metadata.create_all()

        author = Author(first_name='first1', last_name='last1')
        book = Book(title='title1', author_id=author.id, is_available=True)

        s.add(author)
        s.add(book)
        s.commit()

    def tearDown(self):
        s.remove()
        #Base.metadata.drop_all()

class TestModels(TestBase):

    def test_author(self):
        author = s.query(Author).get(1)
        self.assertEqual(author.first_name, 'first1')


if __name__ == '__main__':
    unittest.main()