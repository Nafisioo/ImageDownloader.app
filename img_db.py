import psycopg2
import logging
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

def connect_to_database():
    DB_HOST = os.getenv('DB_HOST', 'postgres')
    DB_PORT = os.getenv('DB_PORT', '5432')
    DB_USER = os.getenv('DB_USER', 'postgres')
    DB_NAME = os.getenv('DB_NAME', 'myimg')

    try:
        connection = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            database=DB_NAME
        )
        return connection
    except (Exception, psycopg2.Error) as error:
        logging.error(f"Error connecting to the database: {error}")
        raise

def insert_image_metadata(connection, url, filename, width, height):
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO images (url, filename, width, height) VALUES (%s, %s, %s, %s)", (url, filename, width, height))
        connection.commit()
    except (Exception, psycopg2.Error) as error:
        logging.error(f"Error inserting image metadata: {error}")
        raise