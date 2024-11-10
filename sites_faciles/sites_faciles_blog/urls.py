from django.urls.conf import path

from sites_faciles.sites_faciles_blog import views


# from sites_faciles.views import SearchResultsView, TagsListView, TagView

# app_name = "sites_faciles_blog"

urlpatterns = [
    path(
        "<str:blog_slug>/categories/<str:category>/feed/",
        views.LatestCategoryFeed(),
        name="category_feed",
    ),
    path("<str:blog_slug>/categories/", views.CategoriesListView.as_view(), name="categories_list"),
    path("<str:blog_slug>/categories/<str:category>/", views.category_view, name="category"),
    path("<str:blog_slug>/tags/<str:tag>/", views.tag_view, name="tag"),
    path("<str:blog_slug>/tags/", views.TagsListView.as_view(), name="tags_list"),
    path("<str:blog_slug>/authors/<int:author_id>/", views.author_view, name="author"),
    path("<str:blog_slug>/archives/<int:year>/", views.year_view, name="archive_year"),
    path(
        "<str:blog_slug>/rss/",
        views.LatestEntriesFeed(),
        name="latest_entries_feed",
    ),
    path(
        "<str:blog_slug>/atom/",
        views.LatestEntriesFeedAtom(),
        name="latest_entries_feed_atom",
    ),
]