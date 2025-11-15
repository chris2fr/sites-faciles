from django import template
from django.conf import settings
from django.contrib.messages.constants import DEBUG, ERROR, INFO, SUCCESS, WARNING
from django.core.paginator import Page
from django.template import Template
from django.template.context import Context
from django.utils.html import format_html, format_html_join

from django_village.checksums import (
    INTEGRITY_CSS,
    INTEGRITY_CSS_ICONS,
    INTEGRITY_FAVICON_APPLE,
    INTEGRITY_FAVICON_ICO,
    INTEGRITY_FAVICON_MANIFEST,
    INTEGRITY_FAVICON_SVG,
    INTEGRITY_JS_MODULE,
    INTEGRITY_JS_NOMODULE,
)
from django_village.utils import find_active_menu_items, generate_random_id, parse_tag_args, village_input_class_attr


register = template.Library()
"""
Tags used in the "village" templates.
"""

# Global tags


@register.inclusion_tag("django_village/global_css.html")
def village_css() -> dict:
    """
    Returns the HTML for the CSS header tags for village

    **Tag name**:
        village_css

    **Usage**:
        `{% village_css %}`
    """
    tag_data = {}
    tag_data["INTEGRITY_CSS"] = INTEGRITY_CSS
    tag_data["INTEGRITY_CSS_ICONS"] = INTEGRITY_CSS_ICONS

    return {"self": tag_data}


@register.inclusion_tag("django_village/global_js.html", takes_context=True)
def village_js(context, *args, **kwargs) -> dict:
    """
    Returns the HTML for the JS body tags for village

    **Tag name**:
        village_js

    **Usage**:
        `{% village_js %}`
    """

    allowed_keys = [
        "nonce",
    ]
    tag_data = parse_tag_args(args, kwargs, allowed_keys)

    tag_data["INTEGRITY_JS_MODULE"] = INTEGRITY_JS_MODULE
    tag_data["INTEGRITY_JS_NOMODULE"] = INTEGRITY_JS_NOMODULE

    return {"self": tag_data}


@register.inclusion_tag("django_village/favicon.html")
def village_favicon() -> dict:
    """
    Returns the HTML for the CSS header tags for the village "Marianne" Favicon

    **Tag name**:
        village_favicon

    **Usage**:
        `{% village_favicon %}`
    """

    tag_data = {}
    tag_data["INTEGRITY_FAVICON_APPLE"] = INTEGRITY_FAVICON_APPLE
    tag_data["INTEGRITY_FAVICON_SVG"] = INTEGRITY_FAVICON_SVG
    tag_data["INTEGRITY_FAVICON_ICO"] = INTEGRITY_FAVICON_ICO
    tag_data["INTEGRITY_FAVICON_MANIFEST"] = INTEGRITY_FAVICON_MANIFEST

    return {"self": tag_data}


@register.inclusion_tag("django_village/theme_modale.html")
def village_theme_modale() -> None:
    """
    Returns the HTML for the theme selection modale for village

    **Tag name**:
        village_theme_modale

    **Usage**:
        `{% village_theme_modale %}`
    """
    return None


# village components


@register.inclusion_tag("django_village/accordion.html")
def village_accordion(*args, **kwargs) -> dict:
    """
    Returns an accordion item. Takes a dict as parameter, with the following structure:

    ```python
    data_dict = {
        "id": "Unique id of the accordion item",
        "title": "Title of the accordion item",
        "content": "Content of the accordion item (can include html)",
        "heading_tag": "(Optional) Heading tag for the accordion title (default: h3)"
    }
    ```

    All of the keys of the dict can be passed directly as named parameters of the tag.

    Can be used alone or in a group with the tag `village_accordion_group`.

    **Tag name**:
        village_accordion

    **Usage**:
        `{% village_accordion data_dict %}`
    """
    allowed_keys = ["id", "title", "content", "heading_tag"]
    tag_data = parse_tag_args(args, kwargs, allowed_keys)

    if "id" not in tag_data:
        tag_data["id"] = generate_random_id("accordion")

    return {"self": tag_data}


@register.inclusion_tag("django_village/accordion_group.html")
def village_accordion_group(items: list) -> dict:
    """
    Returns a group of accordion items. Takes a list of dicts as parameters (see the
    accordion tag for the structure of these dicts.)

    **Tag name**:
        village_accordion_group

    **Usage**:
        `{% village_accordion_group data_list %}`
    """
    return {"self": {"items": items}}


@register.inclusion_tag("django_village/alert.html")
def village_alert(*args, **kwargs) -> dict:
    """
    Returns an alert item. Takes a dict as parameter, with the following structure:

    ```python
    data_dict = {
        "title": "(Optional if small) Title of the alert item",
        "type": "Possible values : info, success, error",
        "content": "(Optional if median) Content of the accordion item (can include html)",
        "heading_tag": "(Optional) Heading tag for the alert title (default: p)",
        "is_collapsible" : "(Optional) Boolean, set to true to add a 'close' button for the alert (default: false)",
        "id": "Unique id of the alert item (Optional, mandatory if collapsible)",
        "extra_classes": "(Optional) string with names of extra classes."
    }
    ```

    All of the keys of the dict can be passed directly as named parameters of the tag.

    Relevant `extra_classes`:

    - `village-alert--sm` : small alert

    On normal (median) alerts, the title is mandatory, the content is optional.
    On small alerts, the title is optional, the content is mandatory.

    **Tag name**:
        village_alert

    **Usage**:
        `{% village_alert data_dict %}`
    """  # noqa

    allowed_keys = [
        "id",
        "title",
        "type",
        "content",
        "heading_tag",
        "is_collapsible",
        "extra_classes",
    ]
    tag_data = parse_tag_args(args, kwargs, allowed_keys)

    tag_data.setdefault("title", None)
    tag_data.setdefault("id", generate_random_id("alert"))
    tag_data.setdefault("is_collapsible", False)

    return {"self": tag_data}


@register.inclusion_tag("django_village/badge.html")
def village_badge(*args, **kwargs) -> dict:
    """
    Returns a badge item. Takes a dict as parameter, with the following structure:

    ```python
    data_dict = {
        "label": "Label of the button item",
        "extra_classes": "(Optional) string with names of extra classes."
    }
    ```


    All of the keys of the dict can be passed directly as named parameters of the tag.

    Relevant extra_classes:

    - `village-badge--sm`: small-sized badge
    - `village-badge--green-menthe` other color codes: change the color of the badge
    - `village-badge--success` (or error/info/warning/new): system badges
    - `village-badge--no-icon`: removes the icon on system badges

    **Tag name**:
        village_badge

    **Usage**:
        `{% village_badge data_dict %}`
    """
    allowed_keys = [
        "label",
        "extra_classes",
    ]
    tag_data = parse_tag_args(args, kwargs, allowed_keys)

    return {"self": tag_data}


@register.inclusion_tag("django_village/badge_group.html")
def village_badge_group(items: list) -> dict:
    """
    Returns a group of badge items. Takes a list of dicts as parameters (see the badge
    tag for the structure of these dicts.)


    **Tag name**:
        village_badge_group

    **Usage**:
        `{% village_badge_group data_list %}`
    """
    return {"self": {"items": items}}


@register.inclusion_tag("django_village/breadcrumb.html", takes_context=True)
def village_breadcrumb(context: Context, tag_data: dict = {}) -> dict:
    """
    Returns a breadcrumb item. Takes a dict as parameter, with the following structure:

    ```python
    data_dict = {
        "links": [{"url": "first-url", "title": "First title"}, {...}],
        "current": "Current page title",
        "root_dir": "the root directory, if the site is not installed at the root of the domain"
    }
    ```

    If the dict is not passed as a parameter, it extracts it from context.

    **Tag name**:
        village_breadcrumb

    **Usage**:
        `{% village_breadcrumb data_dict %}`
    """  # noqa
    if not tag_data:
        if "breadcrumb_data" in context:
            tag_data = context["breadcrumb_data"]
        else:
            tag_data = {}
    return {"self": tag_data}


@register.inclusion_tag("django_village/button.html")
def village_button(*args, **kwargs) -> dict:
    """
    Returns a button item. Takes a dict as parameter, with the following structure:

    ```python
    data_dict = {
        "label": "Label of the button item",
        "onclick": "button action",
        "type": "(Optional) type of button (submit or button - default: submit),
        "name": "(Optional) name of the button",
        "is_disabled": "(Optional) boolean that indicate if the button is activated
        (default: False)",
        "extra_classes": "(Optional) string with names of extra classes."
    }
    ```

    All of the keys of the dict can be passed directly as named parameters of the tag.

    Relevant `extra_classes`:

    - `village-btn--secondary`: secundary button
    - `village-btn--tertiary`: tertiary button
    - `village-btn--tertiary-no-outline`: tertiary button with no outline
    - `village-btn--icon-left` and `village-btn--icon-right`: add an icon to the button
      (associated with an icon class)
    - `village-btn--sm` and `village-btn--lg`: button smaller or larger than the default size

    **Tag name**:
        village_button

    **Usage**:
        `{% village_button data_dict %}`
    """
    allowed_keys = [
        "label",
        "name",
        "type",
        "onclick",
        "is_disabled",
        "extra_classes",
    ]
    tag_data = parse_tag_args(args, kwargs, allowed_keys)

    if "is_disabled" not in tag_data:
        tag_data["is_disabled"] = False
    return {"self": tag_data}


@register.inclusion_tag("django_village/button_group.html")
def village_button_group(*args, **kwargs) -> dict:
    """
    Returns a group of button items. Takes a dict as parameter, with the following structure:

    ```python
    data_dict = {
        "items": "List of dicts (see the button tag for the structure of these dicts.)",
        "extra_classes": "(Optional) string with names of extra classes."
    }
    ```
    Relevant `extra_classes`:

    - `btns-group--inline-sm`: Inline group, small size
    - `btns-group--inline-md`: Inline group, normal size
    - `btns-group--inline-lg`: Inline group, large size
    - `btns-group--sm`: Vertical group, small size
    - `btns-group--lg`: Vertical group, large size
    - `btns-group--equisized`: Width adjusted in Javascript
    - `btns-group--icon-left`: Buttons with an icon on the left side
    - `btns-group--icon-right`: Buttons with an icon on the right side

    **Tag name**:
        village_button_group

    **Usage**:
        `{% village_button_group data_dict %}`
    """
    allowed_keys = [
        "items",
        "extra_classes",
    ]
    tag_data = parse_tag_args(args, kwargs, allowed_keys)

    return {"self": tag_data}


@register.inclusion_tag("django_village/callout.html")
def village_callout(*args, **kwargs) -> dict:
    """
    Returns a callout item. Takes a dict as parameter, with the following structure:

    ```python
    data_dict = {
        "text": "Text of the callout item",
        "title": "(Optional) Title of the callout item",
        "heading_tag": "(Optional) Heading tag for the alert title (default: p)",
        "icon_class": " (Optional) Name of the icon class",
        "extra_classes": "(Optional) string with names of extra classes."
        "button": {                                 # Optional
            "onclick": "button action",
            "label": "button label"
        }
    }
    ```

    All of the keys of the dict can be passed directly as named parameters of the tag.

    Relevant `extra_classes`:

    - Color classes ([See the list](/django_village/resources/colors)), for example `village-callout--green-emeraude`

    **Tag name**:
        village_callout

    **Usage**:
        `{% village_callout data_dict %}`
    """
    allowed_keys = [
        "text",
        "title",
        "heading_tag",
        "icon_class",
        "extra_classes",
        "button",
    ]
    tag_data = parse_tag_args(args, kwargs, allowed_keys)

    return {"self": tag_data}


@register.inclusion_tag("django_village/card.html")
def village_card(*args, **kwargs) -> dict:
    """
    Returns a card item. Takes a dict as parameter, with the following structure:

    ```python
    data_dict = {
        "title": "Title of the card item",
        "heading_tag": "(Optional) Heading tag for the title (h2, etc. Default: p)"
        "description": "Text of the card item",
        "image_url": "(Optional) url of the image",
        "image_alt": "(Optional) alt text of the image",
        "media_badges": "(Optional) list of badges for the media area (similar to a badge_group tag)"
        "new_tab": "(Optional) if True, forces links to open in a new tab",
        "link": "(Optional) link of the card item",
        "enlarge_link": "(Optional) boolean. If true (default), the link covers the whole card",
        "extra_classes": "(Optional) string with names of extra classes",
        "top_detail": "(Optional) dict with a top detail content and optional tags or badges",
        "bottom_detail": "(Optional) a detail string and optional icon",
        "call_to_action": "(Optional) a list of buttons or links at the bottom of the card,
        "id": "(Optional) id of the tile item",
    }
    ```

    All of the keys of the dict can be passed directly as named parameters of the tag.

    Relevant extra classes:

    - `village-card--horizontal`: makes the card horizontal
    - `village-card--horizontal-tier`: allows a 33% ratio instead of the 40% default
    - `village-card--horizontal-half`: allows a 50% ratio instead of the 40% default
    - `village-card--download`: replaces the forward arrow icon with a download one
    - `village-card--grey`: adds a grey background on the card
    - `village-card--no-border`: removes the card border
    - `village-card--no-background`: removes the card background
    - `village-card--shadow`: adds a shadow to the card border

    Format of the top_detail dict (every field is optional):

    ```python
    top_detail = {
        "detail": {
            "text": "the detail text",
            "icon_class": "(Optional) an icon class (eg, village-icon-warning-fill)"
        },
        "tags": "a list of tag items (mutually exclusive with badges)",
        "badges": "a list of badge items (mutually exclusive with tags)"
    }
    ```

    Format of the bottom_detail dict :

    ```python
    bottom_detail = {
        "text": "the detail text",
        "icon_class": "(Optional) an icon class (eg, village-icon-warning-fill)"
    }
    ```


    **Tag name**:
        village_card

    **Usage**:
        `{% village_card data_dict %}`
    """  # noqa
    allowed_keys = [
        "title",
        "heading_tag",
        "description",
        "image_url",
        "image_alt",
        "media_badges",
        "new_tab",
        "link",
        "enlarge_link",
        "extra_classes",
        "top_detail",
        "bottom_detail",
        "call_to_action",
        "id",
    ]
    tag_data = parse_tag_args(args, kwargs, allowed_keys)

    if "enlarge_link" not in tag_data:
        tag_data["enlarge_link"] = True

    if "call_to_action" in tag_data:
        # Forcing the enlarge_link to false if there is a CTA
        tag_data["enlarge_link"] = False

    return {"self": tag_data}


@register.inclusion_tag("django_village/consent.html")
def village_consent(*args, **kwargs) -> dict:
    """
    Returns a consent banner item. Takes a dict as parameter, with the following structure:

    ```python
    data_dict = {
        "title": "Title of the banner",
        "content": "Content of the banner. Can contain HTML."
    }
    ```

    All of the keys of the dict can be passed directly as named parameters of the tag.

    The tag only manages the banner. The logic needs to be implemented.

    **Tag name**:
        village_consent

    **Usage**:
        `{% village_consent data_dict %}`
    """

    allowed_keys = [
        "title",
        "content",
    ]
    tag_data = parse_tag_args(args, kwargs, allowed_keys)

    return {"self": tag_data}


@register.inclusion_tag("django_village/content.html")
def village_content(*args, **kwargs) -> dict:
    """
    Returns a media content item. Takes a dict as parameter, with the following structure:

    ```python
    data_dict = {
        "image_url": "URL of the image file (use either image_url, svg or iframe_url parameter)",
        "svg": "the full content of a SVG file (use either image_url, svg or iframe_url parameter)",
        "iframe": "dictionary with data for an iframe, see below (use either image_url, svg or iframe_url parameter)",
        "caption": "(optional) Caption of the media. Can contain HTML",
        "alt_text": "(optional) Alternative text of the media"
        "extra_classes": "(Optional) string with names of extra classes for the whole component",
        "ratio_class": "(Optional) string with the name of a ratio class",
        "transcription": "(Optional) A transcription item dictionary, see [component documentation](/django_village/components/transcription/)",
    }
    ```

    All of the keys of the dict can be passed directly as named parameters of the tag.

    Structure of the iframe dict:

    ```python
    {
        "title": "The title of the iframe",
        "url": "The URL of the iframe"
        "width": "(optional) The width of the iframe",
        "height": "(optional) The height of the iframe",
        "sandbox": "(optional) a string with the sandbox attribute of the iframe",
        "allow": "(optional) a string with the allow attribute of the iframe",
    }
    ```

    Relevant extra classes:

    - `village-content-media--lg`: media is 125% of the main text width.
    - `village-content-media--sm`: media is 75% of the the main text width.

    Relevant ratio classes for images:

    - `village-ratio-32x9`
    - `village-ratio-16x9`
    - `village-ratio-3x2`
    - `village-ratio-4x3`
    - `village-ratio-1x1`
    - `village-ratio-3x4`
    - `village-ratio-2x3`

    Relevant ratio classes for videos:

    - `village-ratio-16x9`
    - `village-ratio-4x3`
    - `village-ratio-1x1`

    **Tag name**:
        village_content

    **Usage**:
        `{% village_content data_dict %}`
    """

    allowed_keys = [
        "image_url",
        "iframe_url",
        "svg",
        "caption",
        "alt_text",
        "extra_classes",
        "ratio_class",
        "transcription",
    ]

    tag_data = parse_tag_args(args, kwargs, allowed_keys)

    return {"self": tag_data}


@register.inclusion_tag("django_village/france_connect.html")
def village_france_connect(*args, **kwargs) -> dict:
    """
    Returns a FranceConnect button item. Takes a dict as parameter, with the following structure:

    ```python
    data_dict = {
        "id": "(optional) Id of the FranceConnect button item",
        "plus": "(optional) Set to True for FranceConnect+. Default: False"
    }
    ```

    All of the keys of the dict can be passed directly as named parameters of the tag.

    **Tag name**:
        village_france_connect

    **Usage**:
        `{% village_france_connect data_dict %}`
    """

    allowed_keys = [
        "id",
        "plus",
    ]
    tag_data = parse_tag_args(args, kwargs, allowed_keys)

    if "id" not in tag_data:
        tag_data["id"] = generate_random_id("franceconnect")

    if "plus" not in tag_data:
        tag_data["plus"] = False

    return {"self": tag_data}


@register.inclusion_tag("django_village/highlight.html")
def village_highlight(*args, **kwargs) -> dict:
    """
    Returns a highlight item. Takes a dict as parameter, with the following structure:

    ```python
    data_dict = {
        "content": "Content of the highlight item (can include html)",
        "size_class": "(Optional) string with name of text-size related classes",
        "extra_classes": "(Optional) string with names of extra classes",
    }
    ```

    Relevant size_classes:

    - `village-text--sm`
    - `village-text--lg`

    Relevant `extra_classes`:

    - Color classes ([See the list](/django_village/resources/colors)), for example `village-highlight--green-emeraude`

    All of the keys of the dict can be passed directly as named parameters of the tag.

    **Tag name**:
        village_highlight

    **Usage**:
        `{% village_highlight data_dict %}`
    """

    allowed_keys = [
        "content",
        "size_class",
        "extra_classes",
    ]
    tag_data = parse_tag_args(args, kwargs, allowed_keys)

    return {"self": tag_data}


@register.inclusion_tag("django_village/input.html")
def village_input(*args, **kwargs) -> dict:
    """
    Returns a input item. Prefer the use of an actual form (see documentation)

    Takes a dict as parameter, with the following structure:

    ```python
    data_dict = {
        "id": "The unique html id of the input item",
        "label": "Label of the input item",
        "type": "Type of the input item (default: 'text')",
        "onchange": "(Optional) Action that happens when the input is changed",
        "value": "(Optional) Value of the input item",
        "min": "(Optional) Minimum value of the input item (for type='date')",
        "max": "(Optional) Maximum value of the input item (for type='date')",
        "extra_classes": "(Optional) string with names of extra classes"
    }
    ```


    All of the keys of the dict can be passed directly as named parameters of the tag.

    **Tag name**:
        village_input

    **Usage**:
        `{% village_input data_dict %}`
    """

    allowed_keys = [
        "id",
        "label",
        "type",
        "onchange",
        "value",
        "min",
        "max",
        "extra_classes",
    ]
    tag_data = parse_tag_args(args, kwargs, allowed_keys)

    if "id" not in tag_data:
        tag_data["id"] = generate_random_id("input")

    return {"self": tag_data}


@register.inclusion_tag("django_village/link.html")
def village_link(*args, **kwargs) -> dict:
    """
    Returns a link item. Takes a dict as parameter, with the following structure:

    ```python
    data_dict = {
        "url": "URL of the link item",
        "label": "Label of the link item",
        "is_external": "(Optional) Indicate if the link is external",
        "extra_classes": "(Optional) string with names of extra classes"
    }
    ```

    Relevant extra_classes:

    - `village-link--icon-left` or `village-link--icon-right` with an icon class
    - `village-link--sm` for small links
    - `village-link--lg` for large links


    All of the keys of the dict can be passed directly as named parameters of the tag.

    **Tag name**:
        village_link

    **Usage**:
        `{% village_link data_dict %}`
    """

    allowed_keys = [
        "url",
        "label",
        "is_external",
        "extra_classes",
    ]
    tag_data = parse_tag_args(args, kwargs, allowed_keys)

    return {"self": tag_data}


@register.inclusion_tag("django_village/notice.html")
def village_notice(*args, **kwargs) -> dict:
    """
    Returns a notice item. Takes a dict as parameter, with the following structure:

    ```python
    data_dict = {
        "title": "Content of the notice item (can include html)",
        "is_collapsible" : "(Optional) Boolean, set to true to add a 'close' button for the notice (default: false)",
    }
    ```

    All of the keys of the dict can be passed directly as named parameters of the tag.

    **Tag name**:
        village_notice

    **Usage**:
        `{% village_notice data_dict %}`
    """

    allowed_keys = [
        "title",
        "is_collapsible",
    ]
    tag_data = parse_tag_args(args, kwargs, allowed_keys)

    return {"self": tag_data}


@register.inclusion_tag("django_village/pagination.html", takes_context=True)
def village_pagination(context: Context, page_obj: Page) -> dict:
    """
    Returns a pagination item. Takes a Django paginator object as parameter
    Cf. https://docs.djangoproject.com/fr/3.2/topics/pagination/

    **Tag name**:
        village_pagination

    **Usage**:
        `{% village_pagination page_obj %}`
    """
    return {"request": context["request"], "page_obj": page_obj}


@register.inclusion_tag("django_village/quote.html")
def village_quote(*args, **kwargs) -> dict:
    """
    Returns a quote item. Takes a dict as parameter, with the following structure:

    ```python
    data_dict = {
        "text": "Text of the quote",
        "source_url": "(Optional) URL of the source of the quote",
        "author": "(Optional) The author of the quote",
        "source": "(Optional) The name of the source of the quote",
        "details": "(Optional) A list containing detail dicts",
        "image_url": "(Optional) URL of an illustrative image",
        "extra_classes": "(Optional) string with names of extra classes"
    }
    ```

    The `details` dict entries have a mandatory `text` key and an optional `link` key.

    All of the keys of the dict can be passed directly as named parameters of the tag.

    Relevant `extra_classes`:

    - Color classes ([See the list](/django_village/resources/colors)), for example `village-quote--green-emeraude`

    **Tag name**:
        village_quote

    **Usage**:
        `{% village_quote data_dict %}`
    """

    allowed_keys = [
        "text",
        "source_url",
        "author",
        "source",
        "details",
        "image_url",
        "extra_classes",
    ]
    tag_data = parse_tag_args(args, kwargs, allowed_keys)

    return {"self": tag_data}


@register.inclusion_tag("django_village/select.html")
def village_select(*args, **kwargs) -> dict:
    """
    Returns a select item. Prefer the use of an actual form (see documentation)

    Takes a dict as parameter, with the following structure:

    ```python
    data_dict = {
        "id": "The html id of the select item",
        "label": "Label of the select item",
        "onchange": "(Optional) Action that happens when the select is changed",
        "selected": "(Optional) If the item is selected",
        "default": { # Optional
            "disabled": "If the item is disabled",
            "hidden": "If the item is hidden",
        },
        "options": [
            {"text": "Option 1", "value": 1 },
            {"text": "Option 2", "value": 2 }
        ],
        "extra_classes": "(Optional) string with names of extra classes"
    }
    ```
    Relevant extra_classes:

    - `village-sidemenu--sticky`: Makes the menu sticky
    - `village-sidemenu--sticky-full-height`: Makes the menu take the full height of the screen
    - `village-sidemenu--right`: Moves the menu to the right side of the screen

    All of the keys of the dict can be passed directly as named parameters of the tag.

    **Tag name**:
        village_select

    **Usage**:
        `{% village_select data_dict %}`
    """

    allowed_keys = [
        "id",
        "label",
        "onchange",
        "selected",
        "default",
        "options",
        "extra_classes",
    ]
    tag_data = parse_tag_args(args, kwargs, allowed_keys)

    if "id" not in tag_data:
        tag_data["id"] = generate_random_id("select")

    return {"self": tag_data}


@register.inclusion_tag("django_village/sidemenu.html", takes_context=True)
def village_sidemenu(context: Context, *args, **kwargs) -> dict:
    """
    Returns a side menu item. Takes a dict as parameter, with the following structure:

    ```python
    data_dict = {
        "items": "a list of similarly structured dictionaries (see below)",
        "title": "(Optional) The title of the main menu",
        "heading_tag": "(Optional) Heading tag for the accordion title (h2, etc. Default: div)"
        "extra_classes": "(Optional) string with names of extra classes",
    }
    ```

    Item-level-dictionaries items can have either links or a sub-level menu list, and
    it can accept three levels of nested menu entries.

    ```python
    item_dict = {
        "label": "The label of the menu item",
        "items": "(EITHER) a list of similarly structured dictionaries (see below)",
        "link": "(OR) the link (fragment) of the menu item",
    }
    ```

    All of the keys of the dict can be passed directly as named parameters of the tag.

    **Tag name**:
        village_sidemenu

    **Usage**:
        `{% village_sidemenu data_dict %}`
    """

    allowed_keys = ["label", "items", "heading_tag", "extra_classes"]
    tag_data = parse_tag_args(args, kwargs, allowed_keys)

    active_path = context["request"].path
    tag_data["items"], _ = find_active_menu_items(tag_data["items"], active_path)

    return {"self": tag_data}


@register.inclusion_tag("django_village/skiplinks.html", takes_context=True)
def village_skiplinks(context: Context, items: list) -> dict:
    """
    Returns a skiplinks item. Takes a list as parameter, with the following structure:

    ```python
    items = [{ "link": "item1", "label": "First item title"}, {...}]
    ```

    If the list is not passed as a parameter, it extracts it from context.

    **Tag name**:
        village_skiplinks

    **Usage**:
        `{% village_skiplinks items %}`
    """
    if not items:
        if "skiplinks" in context:
            items = context["skiplinks"]
        else:
            items = []
    return {"self": {"items": items}}


@register.inclusion_tag("django_village/stepper.html")
def village_stepper(*args, **kwargs) -> dict:
    """
    Returns a stepper item. Takes a dict as parameter, with the following structure:

    ```python
    data_dict = {
        "current_step_id": "Number of current step",
        "current_step_title": "Title of current step",
        "next_step_title": "(Optional) Title of next step",
        "total_steps": "Total number of steps",
        "heading_tag": "(Optional) Heading tag for the current step title (Default: h2)"
    }
    ```

    All of the keys of the dict can be passed directly as named parameters of the tag.

    **Tag name**:
        village_stepper

    **Usage**:
        `{% village_stepper data_dict %}`
    """
    allowed_keys = [
        "current_step_id",
        "current_step_title",
        "next_step_title",
        "total_steps",
        "heading_tag",
    ]
    tag_data = parse_tag_args(args, kwargs, allowed_keys)

    return {"self": tag_data}


@register.inclusion_tag("django_village/summary.html")
def village_summary(items: list, heading_tag: str = "p") -> dict:
    """
    Returns a summary item. Takes a list as parameter, with the following structure:

    ```python
    items = [
        { "link": "item1", "label": "First item label"},
        { "link": "item2", "label": "Second item label", "children": [
            { "link": "item2-1", "label": "First nested item label"},
            { "link": "item2-2", "label": "Second nested item label"},
            ]},
        {...}
    ]
    ```

    Also takes an optional "heading_tag" parameter, which can be "p" (default) or h2>h6.

    **Tag name**:
        village_summary

    **Usage**:
        `{% village_summary items heading_tag %}`
    """
    return {"self": {"items": items, "heading_tag": heading_tag}}


@register.inclusion_tag("django_village/table.html")
def village_table(*args, **kwargs) -> dict:
    """
    Returns a table item. Takes a dict as parameter, with the following structure:

    ```python
    data_dict = {
        "caption": "The title of the table",
        "content": "A list of rows, each row being a list of cells itself",
        "extra_classes": "(Optional) string with names of extra classes",
        "header": "(Optional) list of cells for the table header."
    }
    ```

    All of the keys of the dict can be passed directly as named parameters of the tag.


    Relevant `extra_classes`:

    - Color classes ([See the list](/django_village/resources/colors)), for example `village-table--green-emeraude`
    - `village-table--bordered`: adds a border under each line
    - `village-table--no-scroll` prevents horizontal scrolling on mobile
    - `village-table--layout-fixed`: forces the table at 100% and equal size columns
    - `village-table--no-caption`: hides the caption
    - `village-table--caption-bottom`: sets the caption after the table instead of before

    **Tag name**:
        village_table

    **Usage**:
        `{% village_table data_dict %}`
    """
    allowed_keys = [
        "caption",
        "content",
        "header",
        "extra_classes",
    ]
    tag_data = parse_tag_args(args, kwargs, allowed_keys)

    return {"self": tag_data}


@register.inclusion_tag("django_village/tag.html")
def village_tag(*args, **kwargs) -> dict:
    """
    Returns a tag item. Takes a dict as parameter, with the following structure:

    ```python
    data_dict = {
        "label": "Label of the tag",
        "link": "(Optional) link of the tag",
        "onclick": "(Optional) action that happens when the tag is clicked on",
        "is_selectable": "(Optional) boolean that marks the tag as selectable",
        "is_dismissable": "(Optional) boolean that marks the tag as dismissable",
        "extra_classes: (Optional) string with names of extra classes"
    }
    ```

    Relevant extra_classes:

    - `village-tag--sm`: for a small tag
    - icon classes: an icon for the tag, along with a positional class
      (eg, `village-icon-arrow-right-line` `village-tag--icon-left`)

    All of the keys of the dict can be passed directly as named parameters of the tag.

    **Tag name**:
        village_highlight

    **Usage**:
        `{% village_highlight data_dict %}`
    """

    allowed_keys = [
        "label",
        "link",
        "onclick",
        "extra_classes",
        "is_selectable",
        "is_dismissable",
    ]
    tag_data = parse_tag_args(args, kwargs, allowed_keys)

    return {"self": tag_data}


@register.inclusion_tag("django_village/tile.html")
def village_tile(*args, **kwargs) -> dict:
    """
    Returns a tile item. Takes a dict as parameter, with the following structure:

    ```python
    data_dict = {
        "title": "Title of the tile item",
        "url": "URL of the link of the tile item",
        "image_path": "path of the tile image",
        "svg_path": "path of the tile image if this is a SVG",
        "description": "(Optional) description of the tile item",
        "detail": "(Optional) detail zone of the tile tiem
        "top_detail": "(Optional) dict with a top detail content and optional tags or badges",
        "heading_tag": "(Optional) Heading tag for the alert title (default: h3)",
        "id": "(Optional) id of the tile item",
        "enlarge_link": "(Optional) boolean. If true (default), the link covers the whole card",
        "extra_classes": "(Optional) string with names of extra classes"
    }
    ```

    All of the keys of the dict can be passed directly as named parameters of the tag.

    Relevant extra_classes:

    - `village-tile--sm`: for a small (SM) tile
    - `village-tile--horizontal`: for an horizontal tile
    - `village-tile--download`: Replaces the forward arrow icon with a download one
    - `village-tile--grey`: adds a grey background on the tile
    - `village-tile--no-border`: removes the tile border
    - `village-tile--no-background`: removes the tile background
    - `village-tile--shadow`: adds a shadow to the tile border


    Format of the top_detail dict (every field is optional):

    ```python
    top_detail = {
        "tags": "a list of tag items (mutually exclusive with badges)",
        "badges": "a list of badge items (mutually exclusive with tags)"
    }
    ```

    Note: `image_path` will work even if a SVG is provided, but `svg_path` will use a
    `<svg>` html tag instead of the `<img>` tag.

    **Tag name**:
        village_tile

    **Usage**:
        `{% village_tile data_dict %}`
    """

    allowed_keys = [
        "title",
        "url",
        "image_path",
        "svg_path",
        "description",
        "detail",
        "top_detail",
        "id",
        "enlarge_link",
        "extra_classes",
    ]
    tag_data = parse_tag_args(args, kwargs, allowed_keys)

    if "enlarge_link" not in tag_data:
        tag_data["enlarge_link"] = True

    return {"self": tag_data}


@register.inclusion_tag("django_village/toggle.html")
def village_toggle(*args, **kwargs) -> dict:
    """
    Returns a toggle item. Takes a dict as parameter, with the following structure:

    ```python
    data_dict = {
        "label": "Label of the item",
        "help_text": "(Optional) string explaining the intended use of the item",
        "is_disabled": '''(Optional) boolean that indicate if the toggle is activated
        (default: False)''',
        "extra_classes": "(Optional) string with names of extra classes",
        "id": "(optional) Id of the item",
    }
    ```

    All of the keys of the dict can be passed directly as named parameters of the tag.

    Relevant extra_classes:

    - `village-toggle--label-left`: sets the label on the left side
    - `village-toggle--border-bottom`: adds a border at the bottom


    **Tag name**:
        village_toggle

    **Usage**:
        `{% village_toggle data_dict %}`
    """

    allowed_keys = [
        "label",
        "help_text",
        "is_disabled",
        "extra_classes",
        "id",
    ]
    tag_data = parse_tag_args(args, kwargs, allowed_keys)

    if "id" not in tag_data:
        tag_data["id"] = generate_random_id("toggle")

    if "is_disabled" not in tag_data:
        tag_data["is_disabled"] = False

    return {"self": tag_data}


@register.inclusion_tag("django_village/tooltip.html")
def village_tooltip(*args, **kwargs) -> dict:
    """
    Returns a tooltip item. Takes a dict as parameter, with the following structure:

    ```python
    data_dict = {
        "content": "Content of the tooltip",
        "label": "(optional) Label of the link item",
        "is_clickable": "(optional) Boolean indicating if this is a button",
        "id": "(optional) Id of the item",
    }
    ```

    All of the keys of the dict can be passed directly as named parameters of the tag.

    **Tag name**:
        village_tooltip

    **Usage**:
        `{% village_tooltip data_dict %}`
    """

    allowed_keys = [
        "content",
        "label",
        "is_clickable",
        "id",
    ]
    tag_data = parse_tag_args(args, kwargs, allowed_keys)

    if "id" not in tag_data:
        tag_data["id"] = generate_random_id("tooltip")

    return {"self": tag_data}


@register.inclusion_tag("django_village/transcription.html")
def village_transcription(*args, **kwargs) -> dict:
    """
    Returns a transcription item. Takes a dict as parameter, with the following structure:

    ```python
    data_dict = {
        "content": "Content of the transcription. Can contain HTML",
        "title": "(optional) A title that appear in the modal. Defaults to 'Transcription'",
        "id": "(optional) Id of the item",
    }
    ```

    All of the keys of the dict can be passed directly as named parameters of the tag.

    **Tag name**:
        village_transcription

    **Usage**:
        `{% village_transcription data_dict %}`
    """

    allowed_keys = [
        "content",
        "title",
        "id",
    ]
    tag_data = parse_tag_args(args, kwargs, allowed_keys)

    if "id" not in tag_data:
        tag_data["id"] = generate_random_id("transcription")

    return {"self": tag_data}


# Extra components


@register.simple_tag(takes_context=True)
def village_django_messages(context, is_collapsible=False, extra_classes=None, wrapper_classes=None):
    """
    Renders django messages in a series a village alerts

    ```python
    data_dict = {
        "is_collapsible" : "(Optional) Boolean, set to true to add a 'close' button for the alert (default: false)",
        "wrapper_classes": "(Optional) extra classes for the wrapper of the alerts (default `village-my-4v`)",
        "extra_classes": "(Optional) extra classes for the alert."
    }
    ```

    All of the keys of the dict can be passed directly as named parameters of the tag.

    Relevant extra_classes:

    - `village-alert--sm` : small alert

    See: [https://docs.djangoproject.com/en/4.2/ref/contrib/messages/](https://docs.djangoproject.com/en/4.2/ref/contrib/messages/)

    By default, the following message level are mapped to the following alert types:

    <div class="village-table" markdown="1">

    Message level | village alert type
    :------------:|:--------------:
    `DEBUG`       | `info`
    `INFO`        | `info`
    `SUCCESS`     | `success`
    `WARNING`     | `warning`
    `ERROR`       | `error`

    </div>

    There types are then concatenated with ``village-alert--`` to form the CSS classe in the template.

    These classes can be modified by setting ``village_MESSAGE_TAGS_CSS_CLASSES`` in your ``settings.py``, like so:

    ```python
    from django.contrib import messages
    village_MESSAGE_TAGS_CSS_CLASSES = {
        messages.DEBUG: "error"
    }
    ```

    You can also use this setting to map [custom custom message levels](https://docs.djangoproject.com/en/4.2/ref/contrib/messages/#creating-custom-message-levels)
    to alert types:

    ```python
    django.conf import global_settings
    from django.contrib import messages
    MESSAGE_TAGS = {
        50: "fatal"
    }
    village_MESSAGE_TAGS_CSS_CLASSES = {
        messages.DEBUG: "debug",
        50: "warning"
    }
    ```

    With this setting, the following code:

    ```python
    messages.add_message(request, 50, "A serious error occurred.")
    ```

    renders an alert with the following CSS class: `village-alert--warning`.

    **Tag name**:
        village_django_messages

    **Usage**:
        `{% village_django_messages data_dict %}`
    """  # noqa

    messages = context.get("messages")

    if not messages:
        return ""

    wrapper_classes = wrapper_classes or "village-my-4v"
    extra_classes = extra_classes or ""

    message_tags_css_classes = {
        DEBUG: "info",
        INFO: "info",
        SUCCESS: "success",
        WARNING: "warning",
        ERROR: "error",
        **getattr(settings, "village_MESSAGE_TAGS_CSS_CLASSES", {}),
    }

    def _render_alert_tag(message):
        return Template("{% load village_tags %}{% village_alert data_dict %}").render(
            Context(
                {
                    "data_dict": {
                        "type": message_tags_css_classes.get(message.level, "info"),
                        "content": str(message),
                        "extra_classes": "{} {}".format(extra_classes, message.extra_tags or "").strip(),
                        "is_collapsible": is_collapsible,
                    }
                }
            )
        )

    return format_html(
        "<div{}>{}</div>",
        format_html(' class="{}"', wrapper_classes) if wrapper_classes else "",
        format_html_join("\n", "{}", ((_render_alert_tag(message),) for message in messages)),
    )


@register.inclusion_tag("django_village/form_snippet.html", takes_context=True)
def village_form(context) -> dict:
    """
    Returns the HTML for a form snippet

    **Tag name**:
        village_form

    **Usage**:
        `{% village_form %}`
    """
    return context


@register.inclusion_tag("django_village/form_field_snippets/field_snippet.html")
def village_form_field(field) -> dict:
    """
    Returns the HTML for a form field snippet

    **Tag name**:
        village_form_field

    **Usage**:
        `{% village_form_field field %}`
    """
    return {"field": field}


register.filter(name="village_input_class_attr", filter_func=village_input_class_attr)


# Other tags and helpers


@register.simple_tag(takes_context=True)
def url_remplace_params(context: Context, **kwargs):
    """
    Allows to make a link that adds or updates a GET parameter while
    keeping the existing ones.
    Useful for combining filters and pagination.

    **Example use**:
    <a href="?{% url_remplace_params page=page_obj.next_page_number %}">Next</a>
    """
    query = context["request"].GET.copy()

    for k in kwargs:
        query[k] = kwargs[k]

    return query.urlencode()


@register.filter
def concatenate(value, arg):
    """Concatenate value and arg"""
    return f"{value}{arg}"


@register.filter
def hyphenate(value, arg):
    """Concatenate value and arg with hyphens as separator, if neither is empty"""
    return "-".join(filter(None, [str(value), str(arg)]))
