from django import template
from django.core.paginator import Page
from django.template.context import Context


register = template.Library()


@register.inclusion_tag("gdvoisins/tags/main_menu_up.html", takes_context=True)
def main_menu_up(context, page, tabindex=0, class_name=""):
    """
    Renders a menu of the given page's immediate children.
    """
    return {
        "class_name": class_name,
        "tabindex": tabindex,
        "menu_items_up": page.get_ancestors().live(),
        "current_page": context.get("self"),
    }


@register.inclusion_tag("gdvoisins/tags/main_menu_down.html", takes_context=True)
def main_menu_down(context, page, tabindex=0, class_name=""):
    """
    Renders a menu of the given page's immediate children.
    """
    return {
        "class_name": class_name,
        "tabindex": tabindex,
        "menu_items_down": page.get_children().live().in_menu(),
        "current_page": context.get("self"),
    }


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


@register.inclusion_tag("gdvoisins/tags/pagination.html", takes_context=True)
def gdvoisins_pagination(context: Context, page_obj: Page) -> dict:
    """
    Returns a pagination item. Takes a Django paginator object as parameter
    Cf. https://docs.djangoproject.com/fr/3.2/topics/pagination/

    **Tag name**:
        village_pagination

    **Usage**:
        `{% village_pagination page_obj %}`
    """
    return {"request": context["request"], "page_obj": page_obj}
