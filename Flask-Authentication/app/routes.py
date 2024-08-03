from flask import request, jsonify
from . import db
from .models import Book

def register_routes(app):
    @app.route('/books', methods=['POST'])
    def add_book():
        data = request.get_json()
        new_book = Book(
            title=data['title'],
            author=data['author'],
            published_year=data['published_year'],
            genre=data['genre'],
            description=data['description']
        )
        db.session.add(new_book)
        db.session.commit()
        return jsonify(new_book.to_dict()), 201

    @app.route('/books/<int:book_id>', methods=['GET'])
    def get_book(book_id):
        book = Book.query.get_or_404(book_id)
        return jsonify(book.to_dict())

    @app.route('/books', methods=['GET'])
    def get_books():
        books = Book.query.all()
        return jsonify([book.to_dict() for book in books])

    @app.route('/books/<int:book_id>', methods=['PUT'])
    def update_book(book_id):
        book = Book.query.get_or_404(book_id)
        data = request.get_json()
        book.title = data.get('title', book.title)
        book.author = data.get('author', book.author)
        book.published_year = data.get('published_year', book.published_year)
        book.genre = data.get('genre', book.genre)
        book.description = data.get('description', book.description)
        db.session.commit()
        return jsonify(book.to_dict())

    @app.route('/books/<int:book_id>', methods=['DELETE'])
    def delete_book(book_id):
        book = Book.query.get_or_404(book_id)
        db.session.delete(book)
        db.session.commit()
        return '', 204

    return app

