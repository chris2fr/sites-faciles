"""Find and (optionally) delete menu items that link to pages whose concrete
model can no longer be resolved (``Page.specific_class`` is ``None``).

This can happen when a page content type's app/model is not registered in the
current ``INSTALLED_APPS`` (e.g. after switching git branches or removing an
app). Rendering any menu then crashes deep inside ``wagtailmenus`` with::

    TypeError: issubclass() arg 1 must be a class

This command repairs the symptom safely: it only touches menu items (never the
pages themselves). Run it with ``--delete`` to actually remove the broken
references; without it, it is a read-only report.
"""

from django.core.management.base import BaseCommand
from wagtailmenus.models.menuitems import FlatMenuItem, MainMenuItem


MENU_ITEM_MODELS = [
    MainMenuItem,
    FlatMenuItem,
]


class Command(BaseCommand):
    help = "Report / delete menu items pointing to pages with an unresolvable content type."

    def add_arguments(self, parser):
        parser.add_argument(
            "--delete",
            action="store_true",
            help="Actually delete the broken menu items (default: report only).",
        )

    def handle(self, *args, **options):
        do_delete = options["delete"]
        broken = []

        for model in MENU_ITEM_MODELS:
            for item in model.objects.select_related("link_page").all():
                page = item.link_page
                if page is None:
                    continue
                try:
                    specific_class = page.specific_class
                except Exception as exc:  # pragma: no cover - defensive
                    broken.append((model, item, page, f"error: {exc!r}"))
                    continue
                if specific_class is None:
                    broken.append((model, item, page, None))

        if not broken:
            self.stdout.write(self.style.SUCCESS("No broken menu items found."))
            return

        self.stdout.write(self.style.WARNING(f"Found {len(broken)} broken menu item(s):"))
        for model, item, page, extra in broken:
            kind = model.__name__
            menu_id = item.menu_id
            ct = page.content_type
            where = f"menu={menu_id} item={item.pk} page_id={page.pk} ({page.title!r})"
            why = extra or f"content_type={ct.app_label}.{ct.model} unresolvable"
            self.stdout.write(f"  - {kind}: {where} -> {why}")

        if not do_delete:
            self.stdout.write(
                self.style.NOTICE(
                    "Read-only report. Rerun with --delete to remove these menu items (the referenced pages are kept)."
                )
            )
            return

        for model, item, page, extra in broken:
            kind = model.__name__
            item_pk = item.pk
            menu_id = item.menu_id
            item.delete()
            self.stdout.write(
                self.style.SUCCESS(
                    f"Deleted {kind} item={item_pk} (page_id={page.pk}, menu={menu_id})."
                )
            )

        self.stdout.write(self.style.SUCCESS("Done."))
