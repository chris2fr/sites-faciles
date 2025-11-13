import argparse
import os

import requests


output_dir = "./output"
host_url = "http://127.0.0.1:8000"
locale = "fr"


def download_image(url, save_path):
    image_response = requests.get(url)
    if image_response.status_code == 200:
        os.makedirs(os.path.dirname(save_path), 0o777, True)
        with open(save_path, "wb") as image_file:
            image_file.write(image_response.content)
        print(f"✅ Image downloaded and saved as {save_path}")
    else:
        print(f"❌ Failed to download image. Status code: {image_response.status_code}")


def get_image(data, image_field_name, output_dir):
    header_image = data.get(image_field_name)
    if header_image:
        header_image_meta = header_image.get("meta")
        if header_image_meta:
            header_image_meta_download_url = header_image_meta.get("download_url")
            if header_image_meta_download_url:
                download_image(
                    f"{host_url}{header_image_meta_download_url}", f"{output_dir}{header_image_meta_download_url}"
                )


def parse_args():
    parser = argparse.ArgumentParser(
        prog="PagesParserAPIv2Wagtail",
        description="Parses Pages from Wagtail",
    )
    parser.add_argument(
        "host_url",
        # required=False,
        type=str,
        help=f"Root HOST URL without trailing / (https://127.0.0.1:8000)",
    )
    parser.add_argument(
        "--locale", required=False, type=str, help=f"Locale (en ou fr)", default="fr", choices=["en", "fr"]
    )
    args = parser.parse_args()
    return {
        "host_url": args.host_url,
        "locale": args.locale,
    }
