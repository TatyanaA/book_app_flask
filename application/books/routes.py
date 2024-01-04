from flask import request, Blueprint
from werkzeug import exceptions
from .controllers import index, create, show, update, destroy

books2 = Blueprint("books2", __name__)

@books2.route('/books', methods=["GET", "POST"])
def handle_books():
    if request.method == "POST": return create()
    if request.method == "GET": return index()

@books2.route('/books/<int:id>', methods=["GET", "PATCH", "DELETE"])
def handle_book(id):
    if request.method == "GET": return show(id)
    if request.method == "PATCH": return update(id)
    if request.method == "DELETE": return destroy(id)

@books2.errorhandler(exceptions.NotFound)
def handle_404(err):
    return { "error": f"Oops {err}"}, 404

@books2.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return { "error": f"Oops {err} "}, 500

@books2.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return { "error": f"Oops {err}" }, 400
