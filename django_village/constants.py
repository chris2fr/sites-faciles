from django.utils.translation import gettext_lazy as _


# List of languages for which the interface translation is currently available
DJANGO_VILLAGE_LANGUAGES = [
    ("en", _("English")),
    ("fr", _("French")),
]

# Color palettes, per https://www.systeme-de-design.gouv.fr/elements-d-interface/fondamentaux-de-l-identite-de-l-etat/couleurs-palette/

COLOR_CHOICES_PRIMARY = [
    ("village-primary", _("Couleur principale")),
    ("village-secondary", _("Couleur secondaire")),
]

COLOR_CHOICES_NEUTRAL = [
    ("grey", _("Grey")),
]

COLOR_CHOICES_SYSTEM = [
    ("info", _("Info")),
    ("success", _("Success")),
    ("warning", _("Warning")),
    ("error", _("Error")),
]

COLOR_CHOICES_ILLUSTRATION = [
    ("village-color3", "Couleur 3"),
    ("village-color4", "Couleur 4"),
    ("village-color5", "Couleur 5"),
    ("village-color6", "Couleur 6"),
    ("village-color7", "Couleur 7"),
    ("village-color8", "Couleur 8"),
    ("village-color9", "Couleur 9"),
    ("village-color10", "Couleur 10"),
    ("village-color11", "Couleur 11"),
    ("village-color12", "Couleur 12"),
    ("village-color13", "Couleur 13"),
    ("village-color14", "Couleur 14"),
    ("village-color15", "Couleur 15"),
    ("village-color16", "Couleur 16"),
    ("village-color17", "Couleur 17"),
    ("village-color18", "Couleur 18"),
    ("village-color19", "Couleur 19"),
    ("village-color20", "Couleur 20"),
]

COLOR_CHOICES = [
    (_("Primary colors"), COLOR_CHOICES_PRIMARY),
    (_("Neutral colors"), COLOR_CHOICES_NEUTRAL),
    (_("Illustration colors"), COLOR_CHOICES_ILLUSTRATION),
]

COLOR_CHOICES_WITH_SYSTEM = [
    (_("Primary colors"), COLOR_CHOICES_PRIMARY),
    (_("Neutral colors"), COLOR_CHOICES_NEUTRAL),
    (_("System colors"), COLOR_CHOICES_SYSTEM),
    (_("Illustration colors"), COLOR_CHOICES_ILLUSTRATION),
]
