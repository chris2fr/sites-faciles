import json
import os
import re

import requests

from .common import host_url, output_dir


# Load JSON from a file
with open("pages.json", "r") as f:
    data = json.load(f)

meta = data.get("meta")
pages = data.get("items")

f.close()


# Check the type of data
print(f"Loaded {len(data)} items and {len(pages)} pages")

# Loop over each entry
for page in pages:
    title = page.get("title")
    meta = page.get("meta")
    slug = meta.get("slug")
    detail_url = meta.get("detail_url")
    id = page.get("id")

    print(f"ID: {id}, Title: {title}, Slug: {slug}, Détails {detail_url}")

    response = requests.get(detail_url)

    if response.status_code == 200:
        page_detail = response.json()
        with open(f"{output_dir}/page_{id}_{slug}.json", "w", encoding="utf-8") as d:
            json.dump(page_detail, d, ensure_ascii=False, indent=2)
        get_image(page_detail, "header_image", output_dir)
        get_image(page_detail, "image", output_dir)
        page_body = page_detail.get("body")
        page_image_srcs = re.findall(r'src="(/[^"]+)"', page_body)
        for image_src in page_image_srcs:
            download_image(f"{host_url}{image_src}", f"{output_dir}/{image_src}")
