from flask import jsonify, request
from werkzeug import exceptions
from .models import Book
from .. import db


def index():
    books = Book.query.all()
    try:
        return jsonify({ "data": [c.json for c in books] }), 200
    except:
        raise exceptions.InternalServerError(f"We are working on it")

def show(id):
    print("id", type(id))
    book = Book.query.filter_by(id=id).first()
    try:
        return jsonify({ "data": book.json }), 200
    except:
        raise exceptions.NotFound(f"You get it")


def create():
    try:
        title,author,genre,publication_year = request.json.values()

        new_book = Book(title,author,genre,publication_year)

        db.session.add(new_book)
        db.session.commit()

        return jsonify({ "data": new_book.json }), 201
    except:
        raise exceptions.BadRequest(f"We cannot process your request")

def update(id):
    data = request.json
    book = Book.query.filter_by(id=id).first()

    for (attribute, value) in data.items():
        if hasattr(book, attribute):
            setattr(book, attribute, value)

    db.session.commit()
    return jsonify({ "data": book.json })

def destroy(id):
    book = Book.query.filter_by(id=id).first()
    db.session.delete(book)
    db.session.commit()
    return "Book Deleted", 204
