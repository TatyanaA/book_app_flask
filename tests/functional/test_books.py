# import json

# # Testing the overall functionality - is the route rendering the correct data?
# def test_index_page(client):
#     response = client.get("/")
#     print(response.data)
#     assert response.status_code == 200
#     assert response.data == b'<p>Hello, World!</p>'
    
# # GET /books
# def test_books_page(client):
#     response = client.get("/books")
#     assert response.status_code == 200
#     data = json.loads(response.data)
    
#     assert data[0]['name'] == 'Test'
#     assert data[0]['age'] == 0
#     assert data[0]['catch_phrase'] == 'I am a test'
    
# # GET/:id books
# def test_book_page(client):
#     response = client.get('/books/2')
#     assert response.status_code == 200
    
#     data = json.loads(response.data)
#     print(data)
#     assert len(data) == 5
#     assert data['id'] == 2
#     assert data['title'] == 'Crime and Punishment'
#     assert data['author'] == "Fyodor Dostoevsky"
#     assert data['genre'] == "Psychological Thriller"
#     assert data['id'] == 1866


