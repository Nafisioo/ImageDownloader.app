import unittest
import img_db

class TestImgDB(unittest.TestCase):
    def setUp(self):
        self.conn = img_db.connect_to_database()

    def tearDown(self):
        self.conn.close()

    def test_connect_to_database(self):
        self.assertIsNotNone(self.conn)

    def test_insert_image_metadata(self):
        img_db.insert_image_metadata(self.conn, 'example.com/image1.jpg', 'image1.jpg', 800, 600)

if __name__ == '__main__':
    unittest.main()
