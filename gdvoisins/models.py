from wagtail.models import Page


class GDVoisinsPage(Page):
    pass

    def get_context(self, request, tag=None, category=None, author=None, year=None, *args, **kwargs):  # NOSONAR
        # context = super(BlogIndexPage, self).get_context(request, *args, **kwargs)
        context = super().get_context(request, *args, **kwargs)
        context["has_drop_down_menu"] = self.get_children().live().in_menu().exists()
        return context
