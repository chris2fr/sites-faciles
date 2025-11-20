from django.db import models
from wagtail.admin.panels import PageChooserPanel
from wagtail.models import Page

from wagtail_village_blog.models import DirectoryIndexPage


class GDVoisinsPage(Page):
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
