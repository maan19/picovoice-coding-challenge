class Book:
    def __init__(self, isbn, title, author, language):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.language = language

    def __eq__(self, other): 
        if not isinstance(other, Book):
            # don't attempt to compare against unrelated types
            return NotImplemented
        return self.isbn == other.isbn and self.title == other.title and self.author == other.author and self.language == other.language
    
    def __str__(self):
        return f"ISBN: {self.isbn}\nTitle: {self.title}\nAuthor: {self.author}\nLanguage: {self.language}"
        