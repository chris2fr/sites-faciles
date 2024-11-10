from django.urls import include, path
from django.utils.translation import gettext_lazy as _
from wagtail import urls as wagtail_urls

from sites_faciles.sites_faciles_blog.urls import urlpatterns as sites_faciles_blog_urlpatterns
from sites_faciles.views import SearchResultsView, TagsListView, TagView


# from django_design_system import urls as django_design_system_urls  # , views
# from django_design_system.sites_faciles_components import ALL_TAGS

# # from django_distill import distill_path
# from wagtail import urls as wagtail_urls


urlpatterns = [
    # Look into search TODO
    path(_("search/"), SearchResultsView.as_view(), name="sites_faciles_search"),
    path("tags/<str:tag>/", TagView.as_view(), name="global_tag"),
    path("tags/", TagsListView.as_view(), name="global_tags_list"),
    path("", include(wagtail_urls)),
] + sites_faciles_blog_urlpatterns