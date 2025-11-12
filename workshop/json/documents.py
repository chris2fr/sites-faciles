import json
import os
import re

import requests
from common import download_image, host_url, output_dir


with open("documents.json", "r") as f:
    data = json.load(f)

meta = data.get("meta")
documents = data.get("items")

for document in documents:
    meta = document.get("meta")
    document_url = meta.get("download_url")
    document_path = re.sub(r"http.?://[^/]+/", "", document_url)
    download_image(f"{document_url}", f"{output_dir}/{document_path}")
