from application.books.models import Book


def test_new_character():
    book = Book("War and Peace", "Leo Tolstoy", "Historical Fiction",1869)
    
    assert book.title == 'War and Peace'
    assert book.author == "Leo Tolstoy"
    assert book.genre == "Historical Fiction"
    assert book.publication_year == 1869


   
