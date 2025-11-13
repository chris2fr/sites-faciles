import html
import json
import os
import re

import requests
from bs4 import BeautifulSoup as bs
from common import download_image, get_image, host_url, output_dir, parse_args


def html_render(html_content):
    if html_content:
        return bs(html_content, features="html.parser").prettify()
    else:
        return ""


def html_image(image_data):
    if image_data:
        href = image_data["meta"].get("download_url")
        return f'<img src="{href}" alt="{image_data["title"]}"/>'
    else:
        return ""


def html_meta_tag(name, val):
    if not val:
        return None
    value = html.escape(str(val))
    value = " ".join(value.splitlines())
    return f'<meta name="{name}" content="{value}"/>'


def html_DirectoryEntryPage(page):
    page_fields = {
        "agenda_item": None,
        "agenda": None,
        "authors": [],
        "blog_categories": [],
        "body": None,
        "date": None,
        "end": None,
        "expire_at": None,
        "extramenu": None,
        "footer1": None,
        "footer2": None,
        "form_fields": [],
        "from_address": None,
        "ghost_filter": None,
        "ghost_include": None,
        "ghost_limit": None,
        "ghost_order": None,
        "ghost_post_tag": None,
        "ghost_tag": None,
        "go_live_at": None,
        "header_color_class": None,
        "header_cta_label": None,
        "header_cta_link": None,
        "header_cta_text": None,
        "header_darken": False,
        "header_image": None,
        "header_large": False,
        "header_with_title": False,
        "id": None,
        "image": None,
        "intro": None,
        "place_url": None,
        "place": None,
        "posts_per_page": None,
        "redirect_url": None,
        "section_1_body": None,
        "section_2_body": None,
        "section_2_description_rich": None,
        "section_3_body": None,
        "section_3_description_rich": None,
        "section1": None,
        "section2": None,
        "section3": None,
        "sections": None,
        "start": None,
        "subject": None,
        "tags": [],
        "thank_you_text": None,
        "theme": None,
        "title": None,
        "to_address": None,
    }
    meta_fields = {
        "type": None,
        "seo_title": None,
        "show_in_menus": False,
        "detail_url": None,
        "html_url": None,
        "search_description": None,
        "first_published_at": None,
        "seo_alias_of": None,
        "tags": [],
        "authors": [],
        "date": None,
        "go_live_at": None,
        "expire_at": None,
        "blog_categories": [],
        "locale": None,
    }
    page_fields_names = {
        "id": "id",
        "title": "title",
        "body": "body",
        "header_image": "og:image",
        "header_with_title": "header_with_title",
        "header_color_class": "header_color_class",
        "header_large": "header_large",
        "header_darken": "header_darken",
        "header_cta_text": "header_cta_text",
        "header_cta_label": "header_cta_label",
        "header_cta_link": "header_cta_link",
    }
    meta = page.get("meta")
    for field in page_fields:
        page_fields[field] = page.get(field)
    for field in meta_fields:
        meta_fields[field] = meta.get(field)
    # if meta_fields["locale"] and meta_fields["locale"] == "en":
    #     host_url = "http://127.0.0.1:8000"
    # else:
    #     host_url = "http://localhost:8000"

    if not meta_fields["seo_title"] or meta_fields["seo_title"] == "":
        meta_fields["seo_title"] = page_fields["title"]

    head_meta_fields = {
        "django_wagtail_type": meta_fields["type"],
        "og:title": meta_fields["seo_title"],
        "og:url": meta_fields["html_url"],
        "og:date": meta_fields["date"],
        "og:description": meta_fields["search_description"],
        # "og:description":" ".join(meta_fields["search_description"].splitlines()),
        "first_published_at": meta_fields["first_published_at"],
        "seo_alias_of": meta_fields["seo_alias_of"],
        "go_live_at": meta_fields["go_live_at"],
        "expire_at": meta_fields["expire_at"],
        "expire_at": page_fields["expire_at"],
        "id": page_fields["id"],
        "show_in_menus": meta_fields["show_in_menus"],
        "detail_url": meta_fields["detail_url"],
        "date": page_fields["date"],
        "start": page_fields["start"],
        "end": page_fields["end"],
        "from_address": page_fields["from_address"],
        "ghost_filter": page_fields["ghost_filter"],
        "ghost_include": page_fields["ghost_include"],
        "ghost_limit": page_fields["ghost_limit"],
        "ghost_order": page_fields["ghost_order"],
        "ghost_post_tag": page_fields["ghost_post_tag"],
        "ghost_tag": page_fields["ghost_tag"],
        "go_live_at": page_fields["go_live_at"],
        "header_color_class": page_fields["header_color_class"],
        "header_cta_label": page_fields["header_cta_label"],
        "header_cta_link": page_fields["header_cta_link"],
        "header_cta_text": page_fields["header_cta_text"],
        "header_darken": page_fields["header_darken"],
        "header_image": page_fields["header_image"],
        "header_large": page_fields["header_large"],
        "header_with_title": page_fields["header_with_title"],
        "image": page_fields["image"],
        "intro": page_fields["intro"],
        "place_url": page_fields["place_url"],
        "place": page_fields["place"],
        "posts_per_page": page_fields["posts_per_page"],
        "redirect_url": page_fields["redirect_url"],
        "subject": page_fields["subject"],
        "thank_you_text": page_fields["thank_you_text"],
        "theme": page_fields["theme"],
        "to_address": page_fields["to_address"],
    }
    head_meta_field_arrays = {
        "tags": {},
        "authors": {},
        "blog_categories": {},
        "form_fields": {},
    }
    for field in head_meta_field_arrays:
        if field in meta_fields and meta_fields[field]:
            for field_item in meta_fields[field]:
                head_meta_field_arrays[field][field_item.get("id")] = field_item.get("meta").get("type")
    call_to_action_html = ""
    if page_fields["header_cta_link"]:
        call_to_action_html = f'<p>{page_fields["header_cta_text"]}<a href="{page_fields["header_cta_link"]}"> {page_fields["header_cta_label"]} </a></p>'
    # title = page.get("title")
    # seo_title = meta.get("seo_title")
    # show_in_menus = meta.get("show_in_menus")
    # type = meta.get("type")
    # detail_url = meta.get("detail_url")
    # html_url = meta.get("html_url")
    # search_description = meta.get("search_description")
    # first_published_at = meta.get("first_published_at")
    # seo_alias_of = meta.get("alias_of")
    # parent = meta.get("parent")
    # header_image = page.get("header_image")
    # header_with_title = page.get("header_with_title")
    # header_color_class = page.get("header_color_class")
    # header_large = page.get("header_large")
    # header_darken = page.get("header_darken")
    # header_cta_text = page.get("header_cta_text")
    # header_cta_label = page.get("header_cta_label")
    # header_cta_link = page.get("header_cta_link")
    # tags = page.get("tags")
    # authors = page.get("authors")
    # date = page.get("date")
    # go_live_at = page.get("go_live_at")
    # expire_at = page.get("expire_at")
    # blog_categories = page.get("blog_categories")
    body_html = html_render(page_fields["body"])
    head_meta = ""
    for field in head_meta_fields:
        if head_meta_fields[field] and not head_meta_fields[field] == "":
            head_meta += html_meta_tag(field, head_meta_fields[field]) + "\n    "
    for field in head_meta_field_arrays:
        for field_item in head_meta_field_arrays[field]:
            if head_meta_field_arrays[field][field_item] and not head_meta_field_arrays[field][field_item] == "":
                head_meta += html_meta_tag(field, head_meta_field_arrays[field][field_item]) + "\n    "
    if page_fields["header_image"]:
        head_meta += html_meta_tag("og:image", page_fields["header_image"]["meta"].get("download_url")) + "\n    "
    elif page_fields["header_image"]:
        head_meta += html_meta_tag("og:image", page_fields["image"]["meta"].get("download_url")) + "\n    "
    return f"""<!DOCTYPE html><html class="no-js" lang="{meta_fields["locale"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="X-UA-Compatible" content="ie=edge">
<html>
<head>
    <title>{title}</title>
    <meta charset="UTF-8">
    {head_meta}
    
</head>
<body>
<header>
{html_render(page_fields["intro"])}
{html_image(page_fields["header_image"])}
{html_image(page_fields["image"])}
<h1>{page_fields["title"]}</h1>
{html_render(page_fields["extramenu"])}
{call_to_action_html}

</header>
<main>
{body_html}
{html_render(page_fields["section1"])}
{html_render(page_fields["section_1_body"])}
{html_render(page_fields["section2"])}
{html_render(page_fields["section_2_body"])}
{html_render(page_fields["section_2_description_rich"])}
{html_render(page_fields["section3"])}
{html_render(page_fields["section_3_body"])}
{html_render(page_fields["section_3_description_rich"])}
{html_render(page_fields["sections"])}
{html_render(page_fields["agenda_item"])}
{html_render(page_fields["agenda"])}
{html_render(page_fields["date"])}
{html_render(page_fields["start"])}
{html_render(page_fields["end"])}
{html_render(page_fields["redirect_url"])}

{html_render(page_fields["place"])}
</main>
<footer>
{html_render(page_fields["footer1"])}
{html_render(page_fields["footer2"])}
</footer>
</body>
</html>
    """


# # Load JSON from a file
# with open("pages.json", "r") as f:
#     data = json.load(f)

args = parse_args()
host_url = args["host_url"]
locale = args["locale"]
api_index_url = f"{host_url}/api/v2/pages/?limit=9999999999999&locale={locale}"

response = requests.get(api_index_url)

if response.status_code == 200:
    data = response.json()

meta = data.get("meta")
pages = data.get("items")

tree = {}

# Check the type of data
print(f"Loaded {len(data)} items and {len(pages)} pages")

os.makedirs(f"{output_dir}/pages", 0o777, True)

# Loop over each entry
for page in pages:
    title = page.get("title")
    meta = page.get("meta")
    slug = meta.get("slug")
    detail_url = meta.get("detail_url")
    id = page.get("id")
    local_detail_url = re.sub(r"http.?://[^/]+", host_url, detail_url)
    print(f"ID: {id}, Title: {title}, Slug: {slug}, Détails {local_detail_url}")

    response = requests.get(local_detail_url)

    if response.status_code == 200:
        page_detail = response.json()

        with open(f"{output_dir}/pages/page_{id}_{slug}.json", "w", encoding="utf-8") as d:
            json.dump(page_detail, d, ensure_ascii=False, indent=2)
        get_image(page_detail, "header_image", output_dir)
        get_image(page_detail, "image", output_dir)
        page_body = page_detail.get("body")
        page_type = page_detail.get("type")
        page_image_srcs = re.findall(r'src="(/[^"]+)"', page_body)
        for image_src in page_image_srcs:
            download_image(f"{host_url}{image_src}", f"{output_dir}{image_src}")
        page_detail_id = page_detail.get("id")
        page_detail_meta = page_detail.get("meta")
        page_detail_meta_html_url = meta.get("html_url")
        parent = page_detail_meta.get("parent")
        if parent:
            parent_id = parent.get("id")
        else:
            parent_id = 0
        if parent_id not in tree:
            tree[parent_id] = []
        tree[parent_id].append(page_detail_id)

        page_path = output_dir + "/sites/" + re.sub(r"http.?://", "", page_detail_meta_html_url)
        print(page_path)
        os.makedirs(os.path.dirname(page_path), 0o777, True)
        with open(f"{page_path}/index.html", "w", encoding="utf-8") as pout:
            pout.write(html_DirectoryEntryPage(page_detail))
    else:
        print(f"Problem with {local_detail_url}")
