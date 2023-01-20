import unittest
from book import Book

class TestBook(unittest.TestCase):
    def test_book_equal(self):
        book1 = Book("1", "Good book for Python", "Jagdeep","English")
        book2 =  Book("1", "Good book for Python", "Jagdeep","English")
        self.assertEqual(book1, book2)
    
    def test_book_not_equal(self):
        book1 = Book("1", "Good book for Python", "Jagdeep","English")
        book2 =  Book("2", "Good book for Python", "Jagdeep","English")
        self.assertNotEqual(book1, book2)

unittest.main()