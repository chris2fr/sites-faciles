from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.template.response import TemplateResponse
from django.utils.translation import gettext_lazy as _
from wagtail.models import Locale, Page, Site


# from django.contrib.sites.models import Site

# To enable logging of search queries for use with the "Promoted search results" module
# <https://docs.wagtail.org/en/stable/reference/contrib/searchpromotions.html>
# uncomment the following line and the lines indicated in the search function
# (after adding wagtail.contrib.search_promotions to INSTALLED_APPS):

# from wagtail.contrib.search_promotions.models import Query


def search(request):
    search_query = request.GET.get("q", None)
    search_query = request.GET.get("query", search_query)
    page = request.GET.get("page", 1)
    locale = Locale.get_active()

    # Search
    if search_query:
        site = Site.find_for_request(request)
        # search_results1 =
        # ContentPage.objects.filter(locale=locale).exclude(exclude_from_search=True).live().search(search_query)
        # search_results2 = FaireMainPage.objects.filter(locale=locale).live().search(search_query)
        # search_results = search_results1 | search_results2
        if search_query[-2:] == " *":
            search_results = (
                Page.objects.filter(sites_rooted_here=site, locale=locale).live().search(search_query[:-2])
            )
        else:
            search_results = (
                Page.objects.filter(sites_rooted_here=site, locale=locale)
                .live()
                .exclude(title__endswith=" *")
                .search(search_query)
            )

        # To log this query for use with the "Promoted search results" module:

        # query = Query.get(search_query)
        # query.add_hit()

    else:
        search_results = Page.objects.none()

    # Pagination
    paginator = Paginator(search_results, 10)
    try:
        search_results = paginator.page(page)
    except PageNotAnInteger:
        search_results = paginator.page(1)
    except EmptyPage:
        search_results = paginator.page(paginator.num_pages)

    return TemplateResponse(
        request,
        "gdvoisins/search/search.html",
        {
            "search_query": search_query,
            "search_results": search_results,
            "locale": locale,
            "full_title": _("Search"),
            "page.title": _("Search"),
        },
    )
