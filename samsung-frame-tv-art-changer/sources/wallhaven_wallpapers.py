import logging
import random
import requests
import subprocess
import os
from io import BytesIO
from typing import Optional, Tuple, Union, List, Dict

def get_image_url(args):
    logging.info('Fetching image list from Wallhaven')
    json_url = args.wallhaven_url

    logging.info(json_url)

    try:
        response = requests.get(json_url)
        response.raise_for_status()
        image_list: dict[list[dict[str, Union[str, dict]]]] = response.json()["data"]
        if not image_list:
            raise ValueError("Empty image list received")

        selected_image: dict[str, Union[str, dict]] = random.choice(image_list)["path"]
        logging.info(selected_image)

        return selected_image
    except (requests.RequestException, ValueError, KeyError) as e:
        logging.error(f"Error getting image url: {str(e)}")
        return None

def get_image(args, image_url) -> Tuple[Optional[BytesIO], Optional[str]]:
    try:
        logging.info(f'Downloading image from {image_url}')
        image_response = requests.get(image_url)
        image_response.raise_for_status()
        image_data = BytesIO(image_response.content)
    
        return image_data, 'JPEG'
    except (requests.RequestException, ValueError, KeyError) as e:
        logging.error(f"Error getting image: {str(e)}")
        return None, None