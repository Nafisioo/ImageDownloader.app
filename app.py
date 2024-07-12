import asyncio
import requests
from bs4 import BeautifulSoup
import img_db
from img_processing import process_images
import os
import psycopg2
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

async def fetch_image_from_url(url):
    response = requests.get(url)
    return response.content

async def fetch_google_image_urls(query):
    google_search_url = f"https://www.google.com/search?q={query}&tbm=isch"
    response = requests.get(google_search_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    image_urls = [img['src'] for img in soup.select('img[data-src]')][:2]  # Extract first 2 image URLs
    return image_urls

async def download_images(image_urls):
    downloaded_images = []
    for url in image_urls:
        try:
            image_data = await fetch_image_from_url(url)
            downloaded_images.append(image_data)
        except Exception as e:
            logging.error(f"Error downloading image from URL: {url}, Error: {e}")
    return downloaded_images

if __name__ == "__main__":
    query = "cute kittens"  # Example search query
    try:
        google_image_urls = asyncio.run(fetch_google_image_urls(query))
        logging.info(f"Found {len(google_image_urls)} image URLs from Google search")
        downloaded_images = asyncio.run(download_images(google_image_urls))
        logging.info(f"Downloaded {len(downloaded_images)} images")
        db_connection = img_db.connect_to_database()
        try:
            asyncio.run(process_images(downloaded_images, google_image_urls, db_connection))
        finally:
            db_connection.close()
            logging.info("Database connection closed")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
