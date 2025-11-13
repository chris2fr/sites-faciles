import html
import os
import re


# === Configuration ===
ROOT_DIR = "./output/"  # Change this if needed
OUTPUT_FILE = os.path.join(ROOT_DIR, "master-pages-index.html")
TITLE = "Master HTML Index"


# === Collect HTML files recursively ===
html_files = []
for dirpath, _, filenames in os.walk(ROOT_DIR):
    for filename in filenames:
        if filename.endswith(".html") and filename != "asfsafsaindex.html":
            full_path = os.path.join(dirpath, filename)
            rel_path = os.path.relpath(full_path, ROOT_DIR)
            html_files.append(rel_path)

# Sort files alphabetically for consistency
html_files.sort()

# === Group files by directory ===
from collections import defaultdict


folders = defaultdict(list)
for path in html_files:
    folder = os.path.dirname(path) or "."
    folders[folder].append(path)

# === Generate HTML index ===
html_lines = [
    "<!DOCTYPE html>",
    "<html lang='en'>",
    "<head>",
    "  <meta charset='UTF-8'>",
    "  <meta name='viewport' content='width=device-width, initial-scale=1.0'>",
    f"  <title>{html.escape(TITLE)}</title>",
    "  <style>",
    "    body { font-family: Arial, sans-serif; margin: 2em; background: #fafafa; }",
    "    h1 { color: #222; }",
    "    h2 { color: #444; margin-top: 1.5em; }",
    "    ul { line-height: 1.6; }",
    "    a { text-decoration: none; color: #007acc; }",
    "    a:hover { text-decoration: underline; }",
    "    .folder { margin-bottom: 1em; }",
    "  </style>",
    "</head>",
    "<body>",
    f"  <h1>{html.escape(TITLE)}</h1>",
    "    <ul>",
]

for folder, files in sorted(folders.items()):
    folder_display = "(root)" if folder == "." else folder
    # if re.match('',folder_display):
    # html_lines.append(f"  <div class='folder'>")
    # html_lines.append(f"    <h2>{html.escape(folder_display)}</h2>")
    # html_lines.append("    <ul>")
    for file_path in files:
        html_lines.append(
            f"      <li><a href='{html.escape(file_path)}' target='_blank'>{html.escape(file_path)}</a></li>"
        )
    # html_lines.append("    </ul>")
    # html_lines.append("  </div>")

html_lines += ["    </ul>", "</body>", "</html>"]

# === Write to index.html ===
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("\n".join(html_lines))

print(f"✅ Master index created at: {OUTPUT_FILE}")
print(f"🔗 Total HTML files indexed: {len(html_files)}")
