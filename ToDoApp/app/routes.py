from flask import request, jsonify
from flask_httpauth import HTTPTokenAuth
from . import db
from .models import User, Todo
from werkzeug.security import generate_password_hash, check_password_hash

def register_routes(app):

    auth = HTTPTokenAuth(scheme='Bearer')

    @auth.verify_token
    def verify_token(token):
        user = User.query.filter_by(token=token).first()
        return user if user else None


    @app.route('/register', methods=['POST'])
    def register_user():
        """Register a new user"""
        data = request.get_json()
        if not data or not data.get('email') or not data.get('password'):
            return jsonify({"message": "Email and password are required"}), 400

        hashed_password = generate_password_hash(data['password'])
        new_user = User(
            username=data['username'],
            name=data['name'],
            email=data['email'],
            password=hashed_password
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user.to_dict()), 201


    @app.route('/login', methods=['POST'])
    def login_user():
        """Login a user and generate a token"""
        data = request.get_json()
        user = User.query.filter_by(email=data['email']).first()
        
        if not user or not check_password_hash(user.password, data['password']):
            return jsonify({"message": "Invalid email or password"}), 401
        db.session.commit()
        return jsonify({'token': user.token}), 200


    @app.route('/users/<int:user_id>', methods=['GET'])
    @auth.login_required
    def get_user(user_id):
        """Retrieve a user by ID"""
        user = User.query.get_or_404(user_id)
        return jsonify(user.to_dict())


    @app.route('/users/<int:user_id>', methods=['PUT'])
    @auth.login_required
    def update_user(user_id):
        """Update user details"""
        user = User.query.get_or_404(user_id)
        data = request.get_json()
        user.username = data.get('username', user.username)
        user.name = data.get('name', user.name)
        user.email = data.get('email', user.email)
        db.session.commit()
        return jsonify(user.to_dict())


    @app.route('/users/<int:user_id>', methods=['DELETE'])
    @auth.login_required
    def delete_user(user_id):
        """Delete a user by ID"""
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted"}), 204


    @app.route('/users/<int:user_id>/todos', methods=['POST'])
    @auth.login_required
    def create_todo(user_id):
        """Create a new todo for a user"""
        user = User.query.get_or_404(user_id)
        data = request.get_json()
        new_todo = Todo(
            user_id=user.id,
            todo=data['todo'],
            status=data.get('status', 'Pending')
        )
        db.session.add(new_todo)
        db.session.commit()
        return jsonify(new_todo.to_dict()), 201


    @app.route('/users/<int:user_id>/todos', methods=['GET'])
    @auth.login_required
    def get_user_todos(user_id):
        """Retrieve all todos for a user"""
        User.query.get_or_404(user_id)
        todos = Todo.query.filter_by(user_id=user_id).all()
        return jsonify([todo.to_dict() for todo in todos])


    @app.route('/todos/<int:todo_id>', methods=['PUT'])
    @auth.login_required
    def update_todo(todo_id):
        """Update a todo by ID"""
        todo = Todo.query.get_or_404(todo_id)
        data = request.get_json()
        todo.todo = data.get('todo', todo.todo)
        todo.status = data.get('status', todo.status)
        todo.finish_date = data.get('finish_date', todo.finish_date)
        db.session.commit()
        return jsonify(todo.to_dict())


    @app.route('/todos/<int:todo_id>', methods=['DELETE'])
    @auth.login_required
    def delete_todo(todo_id):
        """Delete a todo by ID"""
        todo = Todo.query.get_or_404(todo_id)
        db.session.delete(todo)
        db.session.commit()
        return jsonify({"message": "Todo deleted"}), 204
