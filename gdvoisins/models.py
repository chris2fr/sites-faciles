from django.db import models
from wagtail.admin.panels import FieldPanel, PageChooserPanel
from wagtail.fields import RichTextField
from wagtail.models import Page
from wagtail.search import index

from wagtail_village.constants import LIMITED_RICHTEXTFIELD_FEATURES
from wagtail_village_blog.models import DirectoryIndexPage


class GDVoisinsPage(Page):
    body = RichTextField(blank=True, null=True, features=LIMITED_RICHTEXTFIELD_FEATURES)

    search_fields = Page.search_fields + [
        index.SearchField("body"),
    ]

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]

    def get_context(self, request, tag=None, category=None, author=None, year=None, *args, **kwargs):  # NOSONAR
        # context = super(BlogIndexPage, self).get_context(request, *args, **kwargs)
        context = super().get_context(request, *args, **kwargs)
        context["has_drop_down_menu"] = self.get_children().live().in_menu().exists()
        return context


class GDVoisinsAnnuairePage(GDVoisinsPage):
    annuaire_page = models.ForeignKey(DirectoryIndexPage, models.SET_NULL, null=True)

    content_panels = Page.content_panels + [PageChooserPanel("annuaire_page")]

    def get_context(self, request, tag=None, category=None, author=None, year=None, *args, **kwargs):  # NOSONAR
        # context = super(BlogIndexPage, self).get_context(request, *args, **kwargs)
        context = super().get_context(request, *args, **kwargs)
        context.update(self.annuaire_page.process_posts(request, tag=None, category=None, author=None, year=None))
        return context
