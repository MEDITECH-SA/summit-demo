import unittest
from app import app


class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'List of Posts', response.data)

    def test_create_post(self):
        response = self.app.post('/create', data=dict(
            title='Test Post',
            content='This is a test post.'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Post', response.data)

    def test_view_post(self):
        response = self.app.get('/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Post Title', response.data)

    def test_edit_post(self):
        response = self.app.post('/1/edit', data=dict(
            title='Updated Title',
            content='Updated Content'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Updated Title', response.data)
        self.assertIn(b'Updated Content', response.data)

    def test_delete_post(self):
        response = self.app.post('/1/delete', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'Post Title', response.data)


if __name__ == '__main__':
    unittest.main()
