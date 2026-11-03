from django.test import Client, TestCase
from django.urls import reverse

from django_village.models import DjangoVillageConfig


class DjangoVillageConfigTestCase(TestCase):
    def setUp(self) -> None:
        DjangoVillageConfig.objects.create(language="fr", site_title="Titre du site")

    def test_config_is_created(self) -> None:
        test_item = DjangoVillageConfig.objects.first()
        self.assertEqual(test_item.site_title, "Titre du site")

    def test_config_is_not_unique_per_language(self) -> None:
        # The uniqueness on ``language`` was dropped so that the multi-table
        # inheritance model (``WagtailVillageConfig``) can share the same table.
        DjangoVillageConfig.objects.create(language="fr", site_title="Autre titre")
        self.assertEqual(DjangoVillageConfig.objects.filter(language="fr").count(), 2)


class ContextProcessorTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_config_is_none_if_not_created_yet(self) -> None:
        response = self.client.get(reverse("index"))
        self.assertEqual(response.context["SITE_CONFIG"], None)

    def test_config_is_available_to_templates(self) -> None:
        DjangoVillageConfig.objects.create(language="fr", site_title="Titre du site")

        response = self.client.get(reverse("index"))
        self.assertEqual(response.context["SITE_CONFIG"].site_title, "Titre du site")

    def test_config_matches_the_selected_language(self) -> None:
        DjangoVillageConfig.objects.create(language="fr", site_title="Titre du site")
        DjangoVillageConfig.objects.create(language="en", site_title="Site title")

        response = self.client.get("/fr/")
        self.assertEqual(response.context["SITE_CONFIG"].site_title, "Titre du site")

        response = self.client.get("/en/")
        self.assertEqual(response.context["SITE_CONFIG"].site_title, "Site title")

    def test_config_fallbacks_to_first_if_language_is_not_set(self) -> None:
        DjangoVillageConfig.objects.create(language="fr", site_title="Titre du site")

        response = self.client.get(reverse("index"), headers={"accept-language": "en"})
        self.assertEqual(response.context["SITE_CONFIG"].site_title, "Titre du site")
