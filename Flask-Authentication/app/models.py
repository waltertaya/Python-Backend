from . import db

class Book(db.Model):

    __tablename__ = 'books'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    published_year = db.Column(db.Integer)
    genre = db.Column(db.String(50))
    description = db.Column(db.Text)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'published_year': self.published_year,
            'genre': self.genre,
            'description': self.description,
        }
