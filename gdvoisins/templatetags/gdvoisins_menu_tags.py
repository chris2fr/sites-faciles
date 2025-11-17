from django import template


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
