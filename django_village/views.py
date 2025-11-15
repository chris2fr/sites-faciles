import os
from itertools import islice
from textwrap import dedent

import markdown
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.utils.text import slugify
from django.views.decorators.http import require_safe

# /!\ In order to test formset
from django.views.generic import CreateView
from markdown.extensions.codehilite import CodeHiliteExtension

from django_village.context_processors import site_config, urlangs
from django_village.forms import ColorForm

# Used by the module = getattr(globals()["village_tags"], f"village_{tag_name}") line
from django_village.templatetags import village_tags  # noqa

# from django_village.forms import (
#     VillageAuthorCreateForm,
#     VillageBookCreateFormSet,
#     VillageBookCreateFormHelper,
# )
# from django_village.models import VillageAuthor
from django_village.utils import format_markdown_from_file, generate_summary_items
from django_village.village_components import (
    ALL_IMPLEMENTED_COMPONENTS,
    EXTRA_COMPONENTS,
    IMPLEMENTED_COMPONENTS,
    NOT_YET_IMPLEMENTED_COMPONENTS,
    WONT_BE_IMPLEMENTED,
)


def chunks(data, SIZE=10000):
    it = iter(data)
    for _i in range(0, len(data), SIZE):
        yield {k: data[k] for k in islice(it, SIZE)}


def init_payload(page_title: str, request: object, links: list = []):
    # Returns the common payload passed to most pages:
    # title: the page title
    # breadcrumb_data: a dictionary used by the page's breadcrumb
    # skiplinks: a list used by the page's skiplinks item

    breadcrumb_data = {
        "current": page_title,
        "links": links,
        "root_dir": "/django-village",
    }

    skiplinks = [
        {"link": "#content", "label": "Contenu"},
        {"link": "#village-navigation", "label": "Menu"},
    ]

    implemented_component_tags_unsorted = ALL_IMPLEMENTED_COMPONENTS
    implemented_component_tags = dict(
        sorted(implemented_component_tags_unsorted.items(), key=lambda k: k[1]["title"])[:31]
        + [
            (
                "see_all",
                {
                    "title": "Voir tous les composants",
                    "url": "/django_village/components/",
                },
            )
        ]
    )

    mega_menu_categories = chunks(implemented_component_tags, 8)

    data_village_mourning = ""
    current_site_config = site_config(request)["SITE_CONFIG"]
    if current_site_config.mourning:
        data_village_mourning = "data-village-mourning"

    full_title = current_site_config.site_title
    if page_title:
        full_title = page_title + " - " + full_title

    return {
        "title": page_title,
        "menus/mega_menu_categories": mega_menu_categories,
        "breadcrumb_data": breadcrumb_data,
        "skiplinks": skiplinks,
        "langcode": request.LANGUAGE_CODE,
        "data_village_mourning": data_village_mourning,
        "full_title": full_title,
    }


@require_safe
def index(request):
    payload = init_payload("Accueil", request)

    payload["summary_data"] = generate_summary_items(
        [
            "Installation",
            "Utilisation",
            "Développement",
            "Notes",
        ]
    )

    payload["langcode"] = "fr"

    return render(request, "django_village/index.html", payload)


@require_safe
def components_index(request):
    payload = init_payload("Composants", request)
    md = format_markdown_from_file("doc/components.md")
    payload["documentation"] = md["text"]
    payload["implemented_components"] = dict(sorted(IMPLEMENTED_COMPONENTS.items(), key=lambda k: k[1]["title"]))
    payload["extra_components"] = dict(sorted(EXTRA_COMPONENTS.items(), key=lambda k: k[1]["title"]))
    not_yet = dict(sorted(NOT_YET_IMPLEMENTED_COMPONENTS.items(), key=lambda k: k[1]["title"]))
    wont_be = dict(sorted(WONT_BE_IMPLEMENTED.items(), key=lambda k: k[1]["title"]))

    md = markdown.Markdown(
        extensions=[
            "markdown.extensions.fenced_code",
            CodeHiliteExtension(css_class="village-code"),
        ],
    )

    for k, v in not_yet.items():
        if "note" in not_yet[k]:
            not_yet[k]["note"] = md.convert(v["note"]).replace("<p>", "").replace("</p>", "")
    payload["not_yet"] = not_yet

    for k, v in wont_be.items():
        wont_be[k]["reason"] = md.convert(v["reason"]).replace("<p>", "").replace("</p>", "")
    payload["wont_be"] = wont_be
    return render(request, "django_village/components_index.html", payload)


@require_safe
def page_component(request, tag_name):  # NOSONAR
    # First three ifs are required for django-distill
    if tag_name == "footer":
        return page_component_footer(request)
    elif tag_name == "header":
        return page_component_header(request)
    elif tag_name == "follow":
        return page_component_follow(request)
    elif tag_name in ALL_IMPLEMENTED_COMPONENTS:
        current_tag = ALL_IMPLEMENTED_COMPONENTS[tag_name]
        payload = init_payload(
            current_tag["title"],
            request,
            links=[{"url": reverse("components_index"), "title": "Composants"}],
        )
        payload["tag_name"] = tag_name

        # Tag-specific context
        if tag_name == "pagination":
            sample_content = list(range(0, 100))
            paginator = Paginator(sample_content, 10)
            payload["page_obj"] = paginator.get_page(4)
        elif tag_name == "django_messages":
            messages.info(request, "Ceci est une information")
            messages.success(request, "Ceci est un succès")
            messages.warning(request, "Ceci est un avertissement")
            messages.error(request, "Ceci est une erreur")

        module = getattr(globals()["village_tags"], f"village_{tag_name}")
        payload["tag_comment"] = markdown.markdown(
            dedent(module.__doc__),
            extensions=[
                "markdown.extensions.tables",
                "md_in_html",
                "markdown.extensions.fenced_code",
                CodeHiliteExtension(css_class="village-code"),
            ],
        )

        if "sample_data" in current_tag:
            payload["sample_data"] = current_tag["sample_data"]

        if "doc_url" in current_tag:
            payload["doc_url"] = current_tag["doc_url"]

        if "example_url" in current_tag:
            payload["example_url"] = current_tag["example_url"]

        sidemenu_implemented_items = []
        for key, value in ALL_IMPLEMENTED_COMPONENTS.items():
            sidemenu_implemented_items.append(
                {
                    "label": f"{value['title']} ({key})",
                    "link": reverse("page_component", kwargs={"tag_name": key}),
                }
            )

        sidemenu_implemented = {
            "label": "Composants implémentés",
            "items": sidemenu_implemented_items,
        }

        if "/components/" in request.path:
            sidemenu_implemented["is_active"] = True

        payload["side_menu"] = {
            "items": [
                {"label": "Documentation", "link": reverse("components_index")},
                sidemenu_implemented,
                {
                    "label": "Composants non implémentés",
                    "link": reverse("components_index") + "#tabpanel-notyetimplemented-panel",
                },
            ]
        }
        return render(request, "django_village/page_component.html", payload)
    else:
        payload = init_payload("Non implémenté", request)
        payload["not_yet"] = {
            "text": "Le contenu recherché n’est pas encore implémenté",
            "title": "Non implémenté",
        }
        return render(request, "django_village/not_yet.html", payload)


@require_safe
def page_component_header(request):
    payload = init_payload(
        page_title="En-tête",
        request=request,
        links=[{"url": reverse("components_index"), "title": "Composants"}],
    )

    md = format_markdown_from_file("doc/header.md")
    payload["documentation"] = md["text"]
    # payload["summary_data"] = md["summary"]

    return render(request, "django_village/doc_markdown.html", payload)


@require_safe
def page_component_footer(request):
    payload = init_payload(
        page_title="Pied de page",
        request=request,
        links=[{"url": reverse("components_index"), "title": "Composants"}],
    )
    md = format_markdown_from_file("doc/footer.md")
    payload["documentation"] = md["text"]
    # payload["summary_data"] = md["summary"]

    return render(request, "django_village/doc_markdown.html", payload)


@require_safe
def page_component_follow(request):
    payload = init_payload(
        page_title="Lettre d’information et Réseaux Sociaux",
        request=request,
        links=[{"url": reverse("components_index"), "title": "Composants"}],
    )
    md = format_markdown_from_file("doc/follow.md")
    payload["documentation"] = md["text"]
    # payload["summary_data"] = md["summary"]

    return render(request, "django_village/doc_follow.html", payload)


@require_safe
def doc_contributing(request):
    payload = init_payload("Contribuer à Django-village", request)
    md = format_markdown_from_file("CONTRIBUTING.md", ignore_first_line=True)
    payload["documentation"] = md["text"]
    payload["summary_data"] = md["summary"]

    return render(request, "django_village/doc_markdown.html", payload)


@require_safe
def doc_install(request):
    payload = init_payload("Installation de Django-village", request)

    md = format_markdown_from_file("INSTALL.md", ignore_first_line=True)
    payload["documentation"] = md["text"]
    payload["summary_data"] = md["summary"]

    return render(request, "django_village/doc_markdown.html", payload)


@require_safe
def doc_usage(request):
    payload = init_payload("Utiliser Django-village", request)

    md = format_markdown_from_file("doc/usage.md")
    payload["documentation"] = md["text"]
    payload["summary_data"] = md["summary"]

    return render(request, "django_village/doc_markdown.html", payload)


@require_safe
def doc_form(request):
    payload = init_payload("Formulaires – Documentation", request)
    md = format_markdown_from_file("doc/forms.md", ignore_first_line=True)
    payload["documentation"] = md["text"]
    # payload["summary_data"] = md["summary"]

    return render(request, "django_village/doc_markdown.html", payload)


@require_safe
def resource_icons(request):
    payload = init_payload("Icônes", request)

    icons_root = "django_village/static/django_village/dist/icons/"
    icons_folders = os.listdir(icons_root)
    icons_folders.sort()
    all_icons = {}
    summary = []
    for folder in icons_folders:
        files = os.listdir(os.path.join(icons_root, folder))
        files_without_extensions = [f.split(".")[0].replace("village--", "") for f in files]
        files_without_extensions.sort()
        all_icons[folder] = files_without_extensions
        summary.append({"link": f"#{slugify(folder)}", "label": folder.capitalize()})

    payload["icons"] = all_icons
    payload["summary"] = summary

    return render(request, "django_village/page_icons.html", payload)


@require_safe
def resource_pictograms(request):
    payload = init_payload("Pictogrammes", request)

    picto_root = "django_village/static/django_village/dist/artwork/pictograms/"
    picto_folders = os.listdir(picto_root)
    picto_folders.sort()
    all_pictos = {}
    summary = []
    for folder in picto_folders:
        files = os.listdir(os.path.join(picto_root, folder))
        files.sort()
        all_pictos[folder] = files
        summary.append({"link": f"#{slugify(folder)}", "label": folder.capitalize()})

    payload["pictograms"] = all_pictos
    payload["summary"] = summary

    return render(request, "django_village/page_pictograms.html", payload)


@require_safe
def resource_colors(request):
    payload = init_payload("Couleurs", request)

    form = ColorForm()

    payload["form"] = form
    payload["components_data"] = IMPLEMENTED_COMPONENTS

    return render(request, "django_village/page_colors.html", payload)


@require_safe
def search(request):
    payload = init_payload("Recherche", request)

    return render(request, "django_village/search.html", payload)
