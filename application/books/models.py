from application import db, app
app.app_context().push()

class Book(db.Model):
    __tablename__='books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False)
    author = db.Column(db.String(200), nullable=False)
    genre = db.Column(db.String(100), nullable=False)
    publication_year = db.Column(db.Integer)
    

    def __init__(self, title,author,genre,publication_year):    
        self.title=title
        self.author=author
        self.genre=genre
        self.publication_year=publication_year
        

    def __repr__(self):
        return f"Book (id:{self.id}, title:{self.name}, author:{self.author})"

    @property
    def json(self):
        return {"id": self.id, "title": self.title, "author": self.author, "genre": self.genre, "publication_year": self.publication_year}
