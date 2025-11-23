import re


# --- Configuration ---
input_file = "./templates/gdvoisins/fragments/head.html"
output_file = "./templates/gdvoisins/fragments/head.out.html"
replacement_file = "./include/VERSION"

# Regex pattern and replacement text
pattern = r"assets/css/gdvoisins-tailwind[-0-9:a-zA-Z_]*.css"
with open(replacement_file, "r", encoding="utf-8") as f:
    replacement = "assets/css/gdvoisins-tailwind-%s.css" % f.read().rstrip()
    print(replacement)
# ----------------------

with open(input_file, "r", encoding="utf-8") as f:
    text = f.read()

# Perform regex substitution
new_text = re.sub(pattern, replacement, text)

with open(input_file, "w", encoding="utf-8") as f:
    f.write(new_text)

print("Replacement complete. Output saved to", input_file)
