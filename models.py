import os
from sqlalchemy import ForeignKey, Column, String, Integer, \
                    DateTime, create_engine
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
import json
from flask_migrate import Migrate

database_path = os.environ['DATABASE_URL']
if database_path.startswith("postgres://"):
  database_path = database_path.replace("postgres://", "postgresql://", 1)

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()
    migrate = Migrate(app, db)


'''
Book

'''
class Book(db.Model):
  __tablename__ = 'books'

  id = Column(Integer, primary_key=True)
  title = Column(String)
  content = Column(String)
  type = Column(String)
  release_date = Column(DateTime)
  author_id = Column(Integer, ForeignKey('authors.id'), nullable= True)

  def __init__(self, title, content, release_date, type, author_id):
    self.title = title
    self.content = content
    self.type = type
    self.release_date = release_date
    self.author_id = author_id

  
  def insert(self):
    db.session.add(self)
    db.session.commit()

  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'title': self.title,
      'type': self.type,
      'content': self.content,
      'release_date': self.release_date,
      'author_id': self.author_id,
    }


'''
Author
'''

class Author(db.Model):
  __tablename__ = 'authors'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  age = Column(Integer)
  gender = Column(String)
  books = relationship('Books', backref='book', lazy = True)

  def __init__(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender

  
  def insert(self):
    db.session.add(self)
    db.session.commit()

  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'age': self.age,
      'gender': self.gender,
      'books': list(map(lambda book: book.format(), self.books))
    }


