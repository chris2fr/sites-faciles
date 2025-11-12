import json
import os
import re

import requests
from common import download_image, host_url, output_dir


with open("images.json", "r") as f:
    data = json.load(f)

meta = data.get("meta")
images = data.get("items")

for image in images:
    meta = image.get("meta")
    image_path = meta.get("download_url")
    download_image(f"{host_url}{image_path}", f"{output_dir}{image_path}")
