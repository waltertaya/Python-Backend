from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

from flask import request, jsonify
from . import db
from .models import Book, User

def register_routes(app):

    auth = HTTPBasicAuth()

    @auth.verify_password
    def verify_password(username, password):
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            return user
        return None

    @app.route('/register', methods=['POST'])
    def register():
        data = request.get_json()
        user = User.query.filter_by(username=data['username']).first()
        if user:
            return jsonify({'Error': 'User already exists'}), 400
        new_user = User(
            username=data['username'],
            password=generate_password_hash(data['password']),
            name=data['name'],
            email=data['email']
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user.to_dict()), 201

    @app.route('/books', methods=['POST'])
    @auth.login_required
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
    @auth.login_required
    def get_book(book_id):
        book = Book.query.get_or_404(book_id)
        return jsonify(book.to_dict())

    @app.route('/books', methods=['GET'])
    @auth.login_required
    def get_books():
        books = Book.query.all()
        return jsonify([book.to_dict() for book in books])

    @app.route('/books/<int:book_id>', methods=['PUT'])
    @auth.login_required
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
    @auth.login_required
    def delete_book(book_id):
        book = Book.query.get_or_404(book_id)
        db.session.delete(book)
        db.session.commit()
        return '', 204

    return app

