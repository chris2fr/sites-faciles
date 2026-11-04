"""Remap page ``content_type`` rows left over from earlier app renames.

This project was once distributed as ``wagtail_cfran`` / ``blog`` before being
renamed to ``wagtail_village`` / ``wagtail_village_blog``. Pages created back
then still point to the old ``django_content_type`` labels, which are no longer
registered, so ``Page.specific_class`` returns ``None``.

This command finds those pages and repoints their ``content_type`` to the
current equivalent model -- but only when the concrete row for the page exists
in the current model's table (so we never remap a page whose data is gone).

Usage:
    python manage.py remap_orphaned_pages               # read-only report
    python manage.py remap_orphaned_pages --apply       # apply the remap
"""

from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand
from wagtail.models import Page

from wagtail_village.models import ContentPage
from wagtail_village_blog.models import BlogIndexPage


# Old (app_label, model) -> current model class
REMAP = {
    ("wagtail_cfran", "contentpage"): ContentPage,
    ("blog", "blogindexpage"): BlogIndexPage,
}


class Command(BaseCommand):
    help = "Remap pages whose content_type references a renamed/removed app."

    def add_arguments(self, parser):
        parser.add_argument(
            "--apply",
            action="store_true",
            help="Actually update content_type (default: read-only report).",
        )

    def handle(self, *args, **options):
        do_apply = options["apply"]
        found_any = False

        for (old_app, old_model), new_model in REMAP.items():
            old_ct = ContentType.objects.filter(app_label=old_app, model=old_model).first()
            if old_ct is None:
                continue
            new_ct = ContentType.objects.get_for_model(new_model)

            pages = Page.objects.filter(content_type=old_ct)
            if not pages.exists():
                continue
            found_any = True

            self.stdout.write(
                self.style.WARNING(
                    f"'{old_app}.{old_model}' -> '{new_ct.app_label}.{new_ct.model}' "
                    f"({pages.count()} page(s))"
                )
            )

            for page in pages.order_by("id"):
                has_row = new_model.objects.filter(id=page.id).exists()
                status = "OK (data exists)" if has_row else "NO DATA (skip)"
                self.stdout.write(f"  page {page.id} '{page.title}': {status}")

                if do_apply and has_row:
                    Page.objects.filter(id=page.id).update(content_type=new_ct)
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"    -> remapped to {new_ct.app_label}.{new_ct.model}"
                        )
                    )

        if not found_any:
            self.stdout.write(self.style.SUCCESS("No orphaned pages found."))
        elif not do_apply:
            self.stdout.write(
                self.style.NOTICE("Read-only report. Rerun with --apply to remap.")
            )
