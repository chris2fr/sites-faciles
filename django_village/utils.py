import random
import string

import markdown
from django.core.paginator import Page
from django.forms import BoundField, widgets
from django.utils.text import slugify
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.toc import TocExtension


def list_pages(page_obj: Page) -> Page:
    """
    Gets a paginator page item and returns it with a list of pages to display like:
    [1, 2, "…", 17, 18, 19, "…" 41, 42]

    Currently not in use, simpler pages lists are implemented.
    """
    last_page_number = page_obj.paginator.num_pages
    pages_list = [1, 2]
    if page_obj.number > 1:
        pages_list.append(page_obj.number - 1)
    pages_list.append(page_obj.number)
    if page_obj.number < last_page_number:
        pages_list.append(page_obj.number + 1)
    pages_list.append(last_page_number - 1)
    pages_list.append(last_page_number)

    # Keep only one of each
    unique_pages_items = list(set(pages_list))

    list_with_separators = [unique_pages_items[0]]

    for i in range(1, len(unique_pages_items)):
        difference = unique_pages_items[i] - unique_pages_items[i - 1]
        # If "…" would replace only one value, show it instead
        if difference == 2:
            list_with_separators.append(unique_pages_items[i - 1] + 1)
        elif difference > 1:
            list_with_separators.append("…")  # type: ignore
        list_with_separators.append(unique_pages_items[i])

    page_obj.pages_list = list_with_separators
    return page_obj


def parse_tag_args(args, kwargs, allowed_keys: list) -> dict:
    """
    Allows to use a tag with either all the arguments in a dict or by declaring them separately
    """
    tag_data = {}

    if args:
        tag_data = args[0].copy()

    for k in kwargs:
        if k in allowed_keys:
            tag_data[k] = kwargs[k]

    return tag_data


def find_active_menu_items(menu: list, active_path: str) -> tuple:
    """
    Utility function for the village_sidemenu tag: recusively locates the current
    active page and its parent menus and sets them to active
    """
    set_active = False
    for key, item in enumerate(menu):  # Level 1 items
        if "items" in item:
            item["items"], set_active = find_active_menu_items(item["items"], active_path)
            if set_active:
                menu[key]["is_active"] = True
        else:
            if item["link"] == active_path:
                menu[key]["is_active"] = True
                set_active = True
            else:
                menu[key]["is_active"] = False
                set_active = False
    return menu, set_active


def generate_random_id(start: str = ""):
    """
    Generates a random alphabetic id.
    """
    result = "".join(random.SystemRandom().choices(string.ascii_lowercase, k=16))
    if start:
        result = "-".join([start, result])
    return result


def generate_summary_items(sections_names: list) -> list:
    """
    Takes a list of section names and returns them as a list of links
    that can be used with village_summary or village_menu tags.
    """
    items = []
    for section_name in sections_names:
        items.append(
            {
                "label": section_name,
                "link": f"#{slugify(section_name)}",
            }
        )

    return items


def village_input_class_attr(bf: BoundField):
    if not bf.is_hidden and "class" not in bf.field.widget.attrs:
        bf.field.label_suffix = ""
        if isinstance(bf.field.widget, (widgets.Select, widgets.SelectMultiple)):
            bf.field.widget.attrs["class"] = "village-select"
            bf.field.widget.group_class = "village-select-group"
        elif isinstance(bf.field.widget, widgets.RadioSelect):
            bf.field.widget.attrs["village"] = "village"
            bf.field.widget.group_class = "village-radio-group"
        elif isinstance(bf.field.widget, widgets.CheckboxSelectMultiple):
            bf.field.widget.attrs["village"] = "village"
        elif not isinstance(
            bf.field.widget,
            (
                widgets.CheckboxInput,
                widgets.FileInput,
                widgets.ClearableFileInput,
            ),
        ):
            bf.field.widget.attrs["class"] = "village-input"
    return bf


def format_markdown_from_file(filename: str, ignore_first_line: bool = False) -> dict:
    with open(filename) as f:
        md = markdown.Markdown(
            extensions=[
                "markdown.extensions.fenced_code",
                TocExtension(toc_depth="2-6"),
                CodeHiliteExtension(css_class="village-code"),
            ],
        )

        if ignore_first_line:
            content = "".join(f.readlines()[1:]).strip()
        else:
            content = f.read()

        text = md.convert(content)

        toc = md.toc_tokens

        summary = md_format_toc(toc)

        return {"text": text, "summary": summary}


def md_format_toc(toc: dict) -> list:
    # Format the generated TOC into a Django-VILLAGE summary dict
    summary_level = []
    for item in toc:
        if len(item["children"]):
            children = md_format_toc(item["children"])
            summary_level.append({"link": f"#{item['id']}", "label": item["name"], "children": children})
        else:
            summary_level.append({"link": f"#{item['id']}", "label": item["name"]})

    return summary_level


# Lorem ipsum paragraphs
lorem_ipsum = """
<p class="village-mb-2w">
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
    labore et dolore magna aliqua. At quis risus sed vulputate odio ut enim. At risus viverra
    adipiscing at in tellus integer feugiat. Aliquam purus sit amet luctus venenatis lectus.
    Pellentesque id nibh tortor id aliquet lectus proin. Ultricies leo integer malesuada nunc vel
    risus. Euismod elementum nisi quis eleifend quam adipiscing vitae proin. Iaculis eu non diam
    phasellus vestibulum lorem sed risus ultricies. Quis varius quam quisque id diam. Vehicula
    ipsum a arcu cursus vitae congue mauris rhoncus. Sed id semper risus in hendrerit gravida.
</p>

<p class="village-mb-2w">
    Suspendisse potenti nullam ac tortor vitae purus faucibus. Condimentum lacinia quis vel eros.
    Pellentesque sit amet porttitor eget dolor. Varius duis at consectetur lorem donec massa sapien
    faucibus. Egestas pretium aenean pharetra magna ac placerat vestibulum lectus. Tristique magna
    sit amet purus gravida. Nec ullamcorper sit amet risus nullam eget felis eget nunc. Aenean vel
    elit scelerisque mauris pellentesque pulvinar. Vitae proin sagittis nisl rhoncus mattis rhoncus
    urna neque viverra. Quam viverra orci sagittis eu volutpat odio. Sapien faucibus et molestie
    ac. Rhoncus aenean vel elit scelerisque mauris pellentesque pulvinar pellentesque. Nunc sed
    velit dignissim sodales ut eu sem integer.
</p>

<p class="village-mb-2w">
    Diam maecenas ultricies mi eget mauris pharetra et ultrices. Justo nec ultrices dui sapien eget
    mi proin. Viverra mauris in aliquam sem fringilla ut. Pretium lectus quam id leo in vitae
    turpis massa. Ultricies integer quis auctor elit sed vulputate mi sit amet. Non quam lacus
    suspendisse faucibus interdum posuere lorem. Feugiat in fermentum posuere urna nec. Bibendum
    enim facilisis gravida neque. Vitae aliquet nec ullamcorper sit amet risus. Et netus et
    malesuada fames ac turpis. Ut eu sem integer vitae. Aliquam eleifend mi in nulla posuere
    sollicitudin aliquam ultrices sagittis. Eget sit amet tellus cras adipiscing enim. Massa eget
    egestas purus viverra accumsan. Urna neque viverra justo nec. Bibendum est ultricies integer
    quis auctor elit. Sagittis vitae et leo duis ut diam.
</p>

<p class="village-mb-2w">
    Urna porttitor rhoncus dolor purus. Enim eu turpis egestas pretium. Risus ultricies tristique
    nulla aliquet enim tortor at auctor urna. Etiam non quam lacus suspendisse faucibus interdum
    posuere lorem. Ut enim blandit volutpat maecenas volutpat blandit aliquam etiam. Ac tortor
    vitae purus faucibus ornare suspendisse sed nisi lacus. Accumsan lacus vel facilisis volutpat
    est velit egestas dui. Enim eu turpis egestas pretium aenean pharetra. Arcu cursus vitae congue
    mauris rhoncus. A cras semper auctor neque vitae tempus. Viverra ipsum nunc aliquet bibendum
    enim facilisis gravida neque convallis. Ac tortor dignissim convallis aenean et tortor. Sed id
    semper risus in hendrerit gravida rutrum. Tempus iaculis urna id volutpat lacus laoreet.
</p>

<p class="village-mb-2w">
    Massa tempor nec feugiat nisl pretium fusce. Urna porttitor rhoncus dolor purus non enim
    praesent. Suspendisse ultrices gravida dictum fusce. Habitant morbi tristique senectus et netus.
    Adipiscing vitae proin sagittis nisl. Bibendum ut tristique et egestas quis. Dictum non
    consectetur a erat nam at lectus. Vulputate dignissim suspendisse in est ante in nibh mauris
    cursus. Faucibus turpis in eu mi bibendum neque egestas congue quisque. Neque laoreet
    suspendisse interdum consectetur libero id faucibus. Gravida rutrum quisque non tellus orci ac
    auctor augue mauris. Turpis nunc eget lorem dolor sed viverra ipsum nunc. Quam viverra orci
    sagittis eu volutpat odio. Id interdum velit laoreet id donec ultrices tincidunt arcu non.
    Viverra nibh cras pulvinar mattis nunc sed. Risus sed vulputate odio ut enim blandit volutpat
    maecenas volutpat. Augue neque gravida in fermentum et sollicitudin ac orci. Commodo odio
    aenean sed adipiscing diam.
</p>
"""
