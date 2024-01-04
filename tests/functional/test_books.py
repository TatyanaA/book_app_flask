import json

# Testing the overall functionality - is the route rendering the correct data?
def test_index_page(client):
    response = client.get("/")    
    assert response.status_code == 200    
    assert response.data == b'{\n  "message": "Welcome to the book application",\n  "description": "Book API",\n  "endpoints": [\n    "GET /",\n    "GET /books",\n    "GET /books/<int:id>",\n    "POST /books",\n    "PATCH /books/<int:id>",\n    "DELETE /books/<int:id>"\n  ]\n}\n'
    
# GET /books
def test_books_page(client):
    response = client.get("/books")
    assert response.status_code == 200
    data = json.loads(response.data)["data"]
    print(type(data))
    assert type(data) == list
    assert len(data) > 1

    
# GET/:id books
def test_book_page(client):
    response = client.get('/books/2')
    assert response.status_code == 200
    
    data = json.loads(response.data)["data"]
    assert len(data) == 5
    assert data['id'] == 2
    assert data['title'] == 'Crime and Punishment'
    assert data['author'] == "Fyodor Dostoevsky"
    assert data['genre'] == "Psychological Thriller"
    assert data['publication_year'] == 1866


