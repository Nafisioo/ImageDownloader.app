import asyncio
import requests
from bs4 import BeautifulSoup
from img_processing import process_images
import os
import psycopg2

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
        image_data = await fetch_image_from_url(url)
        downloaded_images.append(image_data)
    return downloaded_images

if __name__ == "__main__":
    query = "cute kittens"  # Example search query
    google_image_urls = asyncio.run(fetch_google_image_urls(query))
    downloaded_images = asyncio.run(download_images(google_image_urls))
    asyncio.run(process_images(downloaded_images))



DB_HOST = os.getenv('DB_HOST', 'myhost')
DB_PORT = os.getenv('DB_PORT', '5432')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASS = os.getenv('DB_PASS', '13840131')
DB_NAME = os.getenv('DB_NAME', 'myimg.db')

conn = psycopg2.connect(
    host=DB_HOST,
    port=DB_PORT,
    user=DB_USER,
    password=DB_PASS,
    database=DB_NAME
)
