from cache import LRUCache
from book import Book

cache = LRUCache(4)

#Check cache for the book else call the database, set cache and return book
#In a real life scneraio, this function is probably being run in multiple threads for requests by multiple users, so we can also use locking ion cache in that case
def get_book_info_with_cache(isbn):
    book = cache.get(isbn)
    if book is None:
        book = get_book_info_from_database(isbn)
        cache.put(isbn, book)
    return book
       

#dummy function to get book from database
def get_book_info_from_database(isbn):
    book = Book("1","Good book for Go lang","Jagdeep","English")
    return book


