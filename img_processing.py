import os
from PIL import Image
import img_db
import asyncio
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

async def process_images(downloaded_images, image_urls, db_connection):
    output_dir = "processed_images"
    os.makedirs(output_dir, exist_ok=True)

    valid_image_count = 0

    for i, img_data in enumerate(downloaded_images):
        filename = f"image_{i}.jpg"
        try:
            img = await is_valid_image(img_data)
            if img:
                with img:
                    resized_img = await resize_image(img)
                    resized_img.save(os.path.join(output_dir, filename))

                    img_db.insert_image_metadata(
                        connection=db_connection,
                        url=image_urls[i],
                        filename=filename,
                        width=resized_img.width,
                        height=resized_img.height
                    )
                    valid_image_count += 1
        except ValueError as e:
            logging.error(f"Invalid image data for image {i}: {e}")
        except (IOError, OSError) as e:
            logging.error(f"Error processing image {i}: {e}")
        except Exception as e:
            logging.error(f"Unexpected error processing image {i}: {e}")

    logging.info(f"{valid_image_count}/{len(downloaded_images)} images downloaded, resized, and saved successfully!")

async def is_valid_image(img_data):
    # Implementation to validate image data
    if not img_data:
        raise ValueError("Image data is empty")
    # Rest of the implementation
    return Image.open(img_data)

async def resize_image(img):
    # Implementation to resize image
    return img.resize((224, 224))