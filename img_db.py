#img_db.py
import sqlite3
import unittest
import img_db

def connect_to_database():
    # Establish a connection to the database
    connection = sqlite3.connect('image_metadata.db')
    return connection

def insert_image_metadata(connection, url, filename, width, height):
    # Insert image metadata into the database
    cursor = connection.cursor()
    cursor.execute("INSERT INTO images (url, filename, width, height) VALUES (?, ?, ?, ?)", (url, filename, width, height))
    connection.commit()

class TestImgDB(unittest.TestCase):

    def test_connect_to_database(self):
        conn = img_db.connect_to_database()
        self.assertIsNotNone(conn)

    def test_insert_image_metadata(self):
        conn = img_db.connect_to_database()
        img_db.insert_image_metadata(conn, 'example.com/image1.jpg', 'image1.jpg', 800, 600)
        

if __name__ == '__main__':
    unittest.main()