import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Book, Author

class CastingAgencyTestCase(unittest.TestCase):
    """This class represents the casting agency test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = "postgresql://my_postgres_9p24_user:iuT5Yz7AmDNTsrsoLNMy6nJuoWmEliFQ@dpg-csh4ln3tq21c73e3fkpg-a.oregon-postgres.render.com/my_postgres_9p24"
        if self.database_path.startswith("postgres://"):
            self.database_path = self.database_path.replace("postgres://", "postgresql://", 1)
        setup_db(self.app, self.database_path)

        self.new_book = {
            'title': 'A Brave New World',
            'content': 'A novel written in 1931...',
            'type': 'Science Fiction',
            'release_date': '2024-11-23T19:07:00.000Z',
            'author_id': 2
        }

        self.new_author = {
            'name': 'Aldous Huxley',
            'age': 69,
            'gender': 'Male'
        }

        # # Set up tokens here for testing role-based access control
        self.casting_assistant_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InBHWEVhakU4TXN0WmIyejdwcHpmZSJ9.eyJpc3MiOiJodHRwczovL2Rldi10cmFpbnYudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDY3NDFkOGU3ZmYzYmQ2NjgyMzllNzkyZiIsImF1ZCI6WyJjYXBzdG9uZSIsImh0dHBzOi8vZGV2LXRyYWludi51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNzMyMzY4NzE5LCJleHAiOjE3MzI0NTUxMTksInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJndHkiOiJwYXNzd29yZCIsImF6cCI6ImVrdjFpVDdyZHlwdFJVR2Y2Q0tGUUl1MmtwdW9RVHh1IiwicGVybWlzc2lvbnMiOlsidmlldzphdXRob3JzIiwidmlldzpib29rcyJdfQ.hrCH0PDvoB32cO6axk57oU6mOAejEjOIB26HnfZNh30sNaiScqHyNTjRTA-IfYMSyFaGYCUoJhEElz1F2TqJN-cGySUmE6zWOEWflZFiLp7nJBIptxuiOY_uzCypYeTzmIe-8uW1MYto1rYpmgwK_I7kJRldz4kGrNdG9GWRFrICTSBPNp-eIEr5rLUEGTbc_4zKHAKpYBKHKkjfSRJKS-K6pvADJuk3a6Cn_JtxorrG_J086CGBVGpuiJbXdOtwIkH8QdrWuZRw8NsQ6q_JB03C3YeomuB1-NQKQeeP7zvbq5uHePAKIRGPQkOIArWeq_EXPFn7IPyelbtUicWfTw'
        self.casting_director_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InBHWEVhakU4TXN0WmIyejdwcHpmZSJ9.eyJpc3MiOiJodHRwczovL2Rldi10cmFpbnYudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDY3MDY4NzUxMWVhOWIzYzZlOGEyZDkyMCIsImF1ZCI6WyJjYXBzdG9uZSIsImh0dHBzOi8vZGV2LXRyYWludi51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNzMyMzYxNTA5LCJleHAiOjE3MzI0NDc5MDksInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJndHkiOiJwYXNzd29yZCIsImF6cCI6ImVrdjFpVDdyZHlwdFJVR2Y2Q0tGUUl1MmtwdW9RVHh1IiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmF1dGhvcnMiLCJkZWxldGU6Ym9va3MiLCJwb3N0OmF1dGhvcnMiLCJwb3N0OmJvb2tzIiwidXBkYXRlOmF1dGhvcnMiLCJ1cGRhdGU6Ym9va3MiLCJ2aWV3OmF1dGhvcnMiLCJ2aWV3OmJvb2tzIl19.5r0MHTcsC-LkfCa-mpMkAh2eeJ4ocRLi_lTZ1REknGx-a4h4z4x_v7ax1GcFQXhLSdzrRYtrBD3c71q9VhlThSfggECIjh3TVm-MnbzcinJ5jr9AtKZzADkPTOK7cnQu2eLvYYOOW6YMo38ccwqmYWexCC1xP7vHa81fOFAIf4zuhlgeus9qqo9w92Lf6v09eVsOqiosqZixK5T1418c3eil-tR6aVD8FE87zvkyU-HqlLCidlWS13I7kTcovaGxz8Frm5uqphN6KB6HgnbTNZMNCv6RcyZg42St4Hvyc8hu6aRAEBfaOQzt39xOt3GBc1SJsUhSTA8Ezo2QFvM7wA'

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    def get_headers(self, token):
        return {'Authorization': 'Bearer ' + token}

    # Test cases for Books
    def test_get_books_success(self):
        """Test success for getting books"""
        res = self.client().get('/books', headers=self.get_headers(self.casting_assistant_token))
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['books'])

    def test_get_books_unauthorized(self):
        """Test failure for getting books without permission"""
        res = self.client().get('/books')
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])

    def test_create_book_success(self):
        """Test success for creating a new book"""
        res = self.client().post('/books', json=self.new_book, headers=self.get_headers(self.casting_director_token))
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_create_book_bad_request(self):
        """Test failure for creating a new book with missing data"""
        res = self.client().post('/books', json={}, headers=self.get_headers(self.casting_director_token))
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 400)
        self.assertFalse(data['success'])

    def test_delete_book_success(self): 
        """Test success for deleting a book""" 
        # Create a new book first
        res = self.client().post('/books', json=self.new_book, headers=self.get_headers(self.casting_director_token)) 
        data = json.loads(res.data) 
        book_id = data['book_id'] # Delete the newly created book 
        res = self.client().delete(f'/books/{book_id}', headers=self.get_headers(self.casting_director_token)) 
        data = json.loads(res.data) 
        self.assertEqual(res.status_code, 200) 
        self.assertTrue(data['success']) 
        self.assertEqual(data['book_id'], book_id)

    def test_delete_book_not_found(self):
        """Test failure for deleting a non-existent book"""
        res = self.client().delete('/books/9999', headers=self.get_headers(self.casting_director_token))
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])

    # Test cases for Authors
    def test_get_authors_success(self):
        """Test success for getting authors"""
        res = self.client().get('/authors', headers=self.get_headers(self.casting_assistant_token))
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['authors'])

    def test_get_authors_unauthorized(self):
        """Test failure for getting authors without permission"""
        res = self.client().get('/authors')
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])

    def test_create_author_success(self):
        """Test success for creating a new author"""
        res = self.client().post('/authors', json=self.new_author, headers=self.get_headers(self.casting_director_token))
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_create_author_bad_request(self):
        """Test failure for creating a new author with missing data"""
        res = self.client().post('/authors', json={}, headers=self.get_headers(self.casting_director_token))
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 400)
        self.assertFalse(data['success'])

    def test_delete_author_success(self):
        """Test success for deleting an author"""
        # Create a new author first
        res = self.client().post('/authors', json=self.new_author, headers=self.get_headers(self.casting_director_token))
        data = json.loads(res.data)
        author_id = data['author_id']
    
        # Delete the newly created author
        res = self.client().delete(f'/authors/{author_id}', headers=self.get_headers(self.casting_director_token))
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['author_id'], author_id)


    def test_delete_author_not_found(self):
        """Test failure for deleting a non-existent author"""
        res = self.client().delete('/authors/9999', headers=self.get_headers(self.casting_director_token))
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])

    # Role-based access control tests
    def test_create_author_role_based_access(self):
        """Test failure for creating an author with a role that lacks permission"""
        res = self.client().post('/authors', json=self.new_author, headers=self.get_headers(self.casting_assistant_token))
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 401)  # Forbidden
        self.assertFalse(data['success'])
if __name__ == "__main__":
    unittest.main()

