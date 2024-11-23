import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Book, Author

from auth.auth import AuthError, requires_auth

from datetime import datetime

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers',
            'Content-Type,Authorization,true')
        response.headers.add(
            'Access-Control-Allow-Methods',
            'GET,PUT,POST,DELETE,OPTIONS')
        return response

    @app.route('/books', methods=['GET'])
    @requires_auth('view:books')
    def get_books(payload):
        books = Book.query.all()
        print(str(books)+ " books ====")
        books = list(map(lambda book: book.format(), books))
        return jsonify({
            "success": True,
            "books": books
        })


    @app.route('/authors', methods=['GET'])
    @requires_auth('view:authors')
    def get_authors(payload):
        authors = Actor.query.all()
        print(str(authors)+ " authors ====")
        authors = list(map(lambda author: author.format(), authors))
        return jsonify({
            "success": True,
            "authors": authors
        })

    
    @app.route('/books', methods=['POST'])
    @requires_auth('post:books')
    def create_book(payload):
        body = request.get_json()

        print(str(body)+ " body ====")
        if body is None:
            abort(400)

        title = body.get('title', None)
        content = body.get('content', None)
        type = body.get('type', None)
        release_date = body.get('release_date', None)
        author_id = body.get('author_id', None)
        print(str(title)+ " title ====")
        print(str(content)+ " content ====")
        print(str(type)+ " type ====")
        print(str(release_date)+ " release_date ====")
        print(str(author_id)+ " author_id ====")

        if title is None or content is None or release_date is None or type is None or author_id is None:
            abort(400, "Body Error")

        book = Book(title=title, content = content,release_date=release_date, type = type, author_id=author_id )

        book.insert()

        return jsonify({
            "success": True
        })


    @app.route('/authors', methods=['POST'])
    @requires_auth('post:authors')
    def create_author(payload):
        body = request.get_json()

        print(str(body)+ " body ====")

        if body is None:
            abort(400)

        name = body.get('name', None)
        age = body.get('age', None)
        gender = body.get('gender', None)
        print(str(name)+ " name ====")
        print(str(age)+ " name ====")
        print(str(gender)+ " name ====")

        if name is None or age is None or gender is None:
            abort(400, "Body Error")

        author = Author(name=name, age=age, gender=gender)

        author.insert()

        return jsonify({
            "success": True
        })


    @app.route('/books/<int:book_id>', methods=['DELETE'])
    @requires_auth('delete:books')
    def delete_book(payload, book_id):
        book = Book.query.filter(Book.id == book_id).one_or_none()

        if book is None:
            abort(404, "Not found book " + str(book_id))

        book.delete()

        return jsonify({
            'success': True,
            'book_id': book_id
        })


    @app.route('/authors/<int:author_id>', methods=['DELETE'])
    @requires_auth('delete:authors')
    def delete_author(payload, author_id):
        author = Author.query.filter(Author.id == author_id).one_or_none()

        if author is None:
            abort(404, "Not found author" + str(author_id))

        author.delete()

        return jsonify({
            'success': True,
            'author_id': author_id
        })


    @app.route('/books/<int:book_id>', methods=['PATCH'])
    @requires_auth('update:books')
    def update_book(payload, book_id):

        book_update = Book.query.get(book_id)

        if not book_update:
            abort(404,'Book id' + str(book_id) + ' can not found!')

        body = request.get_json()

        title = body.get('title', None)
        content = body.get('content', None)
        type = body.get('type', None)
        release_date = body.get('release_date', None)
        author_id = body.get('author_id', None)

        if title:
            updated_book.title = title
        if content:
            updated_book.content = content
        if type:
            updated_book.type = type
        if release_date:
            updated_book.release_date = release_date
        if author_id:
            author_update.author_id = author_id

        book_update.update()

        return jsonify({
            "success": True,
            "book": book_update.format()
        })


    @app.route('/authors/<int:author_id>', methods=['PATCH'])
    @requires_auth('update:authors')
    def update_author(payload, author_id):

        author_update = Author.query.get(author_id)

        if not author_update:
            abort(404,'Author id: ' + str(author_id) +' can not found!')

        body = request.get_json()

        name = body.get('name', None)
        age = body.get('age', None)
        gender = body.get('gender', None)

        if name:
            author_update.name = name
        if age:
            author_update.age = age
        if gender:
            author_update.gender = gender
        

        try:
            author_update.update()
        except BaseException:
            abort( 400, "format error" + str(author_id))

        return jsonify({
            "success": True,
            "author": author_update.format()
        })

    # Error Handling
    '''
    Example error handling for unprocessable entity
    '''


    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422


    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'resource not found'
        }), 404


    @app.errorhandler(AuthError)
    def auth_error(error):
        return jsonify({
            'success': False,
            'error': error.status_code,
            'message': error.error['description']
        }), error.status_code


    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            'success': False,
            'error': 401,
            'message': 'Unathorized'
        }), 401


    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            'success': False,
            'error': 500,
            'message': 'internal server error'
        }), 500


    @app.errorhandler(400)
    def bad_request(error):
        print(error)
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'bad request'
        }), 400


    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            'success': False,
            'error': 405,
            'message': 'method is not allowed'
        }), 405
    return app

app = create_app()

if __name__ == '__main__':
    app.run()
