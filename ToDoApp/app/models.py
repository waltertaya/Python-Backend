from app import db, gen_token
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    token = db.Column(db.Text, nullable=True, default=gen_token())

    todos = db.relationship('Todo', backref='user', lazy=True)

    def to_dict(self):
        return {
            'user_id': self.id,
            'username': self.username,
            'name': self.name,
            'email': self.email,
            'token': self.token
        }

class Todo(db.Model):
    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    todo = db.Column(db.String(80), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='Pending')  # Define statuses like 'Pending', 'In Progress', 'Completed'
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    finish_date = db.Column(db.DateTime, nullable=True)

    def to_dict(self):
        return {
            'todo_id': self.id,
            'user_id': self.user_id,
            'todo': self.todo,
            'status': self.status,
            'created_date': self.created_date.isoformat() if self.created_date else None,
            'finish_date': self.finish_date.isoformat() if self.finish_date else None
        }
