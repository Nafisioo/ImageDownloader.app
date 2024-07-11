# test_img_db.py
import unittest
import img_db

class TestImgDB(unittest.TestCase):

    def test_connect_to_database(self):
        conn = img_db.connect_to_database()
        self.assertIsNotNone(conn)

    def test_insert_image_metadata(self):
        conn = img_db.connect_to_database()
        img_db.insert_image_metadata(conn, 'example.com/image1.jpg', 'image1.jpg', 800, 600)

if __name__ == '__main__':
    unittest.main()
