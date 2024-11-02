"""
Django settings for lesgrandsvoisins project.

Generated by 'django-admin startproject' using Django 5.0.9.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url # Pour un syntaxe différent de base de données
from dotenv import load_dotenv # Pour les variables d'.env

# Prendre les variables d'environnement
load_dotenv()

# Check to see if basic variables needed are defined

REQUIRED = ["DATABASE_URL","SITE_NAME","SECRET_KEY", "WAGTAILTRANSFER_SECRET_KEY","HOST_URL"]

needs_required = []
for i in REQUIRED:
  if not os.getenv(i) != '':
    needs_required.append(i)

if needs_required != []:
  raise ValueError("Merci de mettre les variables suivantes dans .env: %s" % ', '.join(needs_required))


PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True if os.getenv("DEBUG") == "True" else False
DEBUG_TOOLBAR = True if os.getenv("DEBUG_TOOLBAR") == "True" else False

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "127.0.0.1, localhost").replace(" ", "").split(",")

HOST_URL = os.getenv("HOST_URL", "localhost")

# Application definition

SITE_ID = 1

INSTALLED_APPS = [
  "allauth",
  "allauth.account",
  "allauth.socialaccount",
  "lesgrandsvoisins",
  "lesgv",
  "django_village.theme_designsystem",
  "django_village.theme_lesgrandsvoisins",
  "django_village",
  "django.contrib.admin",
  "django.contrib.auth",
  "django.contrib.contenttypes",
  "django.contrib.messages",
  "django.contrib.sessions",
  "django.contrib.staticfiles",
  "modelcluster",
  "sass_processor",
  "search",
  "storages",
  "taggit",
  "wagtail_localize.locales",
  "wagtail_localize",
  "wagtail_transfer",
  "wagtail_village_blog",
  "wagtail_village_dashboard",
  "wagtail_village_forms",
  "wagtail_village_lesgrandsvoisins",
  "wagtail_village",
  "wagtail.admin",
  "wagtail.contrib.forms",
  "wagtail.contrib.redirects",
  "wagtail.contrib.settings",
  "wagtail.documents",
  "wagtail.embeds",
  "wagtail.images",
  "wagtail.search",
  "wagtail.sites",
  "wagtail.snippets",
  "wagtail.users",
  "wagtail",
  "wagtailmarkdown",
  "wagtailmenus",
  "widget_tweaks",
]

# Only add these on a dev machine
# if DEBUG and "localhost" in HOST_URL:
if DEBUG:
  INSTALLED_APPS += [
    "django_extensions",
    "wagtail.contrib.styleguide",
  ]

if DEBUG_TOOLBAR:
  INSTALLED_APPS += [
    "debug_toolbar",  
  ]

MIDDLEWARE = [
  "django.contrib.sessions.middleware.SessionMiddleware",
  "django.middleware.common.CommonMiddleware",
  "django.middleware.csrf.CsrfViewMiddleware",
  "django.contrib.auth.middleware.AuthenticationMiddleware",
  "django.contrib.messages.middleware.MessageMiddleware",
  "django.middleware.clickjacking.XFrameOptionsMiddleware",
  "django.middleware.locale.LocaleMiddleware", # Ajouté pour la localisation
  "django.middleware.security.SecurityMiddleware",
  "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]

MIDDLEWARE += [
  "allauth.account.middleware.AccountMiddleware",
]

# if DEBUG and "localhost" in HOST_URL:
if DEBUG_TOOLBAR:
  MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
  ]

ROOT_URLCONF = "lesgrandsvoisins.urls"

TEMPLATES = [
  {
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "DIRS": [
      os.path.join(BASE_DIR, "django_village/templates"), # Pour Django_Village
      os.path.join(PROJECT_DIR, "templates"),
      os.path.join(BASE_DIR, "wagtail_village_blog/templates"), # Pour wagtail_village_
      os.path.join(BASE_DIR, "wagtail_village_dashbord/templates"), # Pour wagtail_village_
      os.path.join(BASE_DIR, "wagtail_village_forms/templates"), # Pour wagtail_village_
      os.path.join(BASE_DIR, "wagtail_village_lesgrandsvoisins/templates"), # Pour wagtail_village_
      os.path.join(BASE_DIR, "wagtail_village/templates"),
    ],
    "APP_DIRS": True,
    "OPTIONS": {
      "context_processors": [
        "django_village.context_processors.site_config", # Ajouté
        "django.contrib.auth.context_processors.auth",
        "django.contrib.messages.context_processors.messages",
        "django.template.context_processors.debug",
        "django.template.context_processors.request",
        "wagtail_village.context_processors.mega_menus", # Ajouté
        "wagtail_village.context_processors.sitevars", # Ajouté
        "wagtail_village.context_processors.skiplinks", # Ajouté
        "wagtail_village.context_processors.urlangs", # Ajouté
        "wagtail.contrib.settings.context_processors.settings", # Ajouté
        "wagtailmenus.context_processors.wagtailmenus", # Ajouté
      ],
    },
  },
]

WSGI_APPLICATION = "lesgrandsvoisins.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASE_URL = os.getenv("DATABASE_URL") # Lire depuis .env

if DATABASE_URL:
  DATABASES = {
    "default":dj_database_url.parse(
        DATABASE_URL,
        conn_max_age=600,
        conn_health_checks=True,
      )
  }
else:
  raise ValueError("Please set the DATABASE_URL environment variable")

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
  {
    "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
  },
  {
    "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
  },
  {
    "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
  },
  {
    "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
  },
]

WAGTAIL_PASSWORD_RESET_ENABLED = os.getenv("WAGTAIL_PASSWORD_RESET_ENABLED", False) # Ajouté

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "fr-fr"

TIME_ZONE = "Europe/Paris"

USE_I18N = True

USE_TZ = True

WAGTAIL_I18N_ENABLED = True # Ajouté pour I18N

WAGTAIL_CONTENT_LANGUAGES = LANGUAGES = [ # Ajouté pour I18N
  ("en", "English"),
  ("fr", "French"),
]

STORAGES = {}

if os.getenv("S3_HOST"):
  endpoint_url = f"{os.getenv('S3_PROTOCOL', 'https')}://{os.getenv('S3_HOST')}"
  STORAGES["default"] = {
    "BACKEND": "storages.backends.s3.S3Storage",
    "OPTIONS": {
      "bucket_name": os.getenv("S3_BUCKET_NAME", "set-bucket-name"),
      "access_key": os.getenv("S3_KEY_ID", "123"),
      "secret_key": os.getenv("S3_KEY_SECRET", "secret"),
      "endpoint_url": endpoint_url,
      "region_name": os.getenv("S3_BUCKET_REGION", "fr"),
      "file_overwrite": False,
      "location": os.getenv("S3_LOCATION", ""),
    },
  }
  MEDIA_URL = f"{endpoint_url}/"
else:
  # Default storage settings, with the staticfiles storage updated.
  # See https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STORAGES
  # ManifestStaticFilesStorage is recommended in production, to prevent
  # outdated JavaScript / CSS assets being served from cache
  # (e.g. after a Wagtail upgrade).
  # See https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/#manifeststaticfilesstorage
  STORAGES["default"] = {
    "BACKEND": "django.core.files.storage.FileSystemStorage",
  }
  MEDIA_URL = "/medias/" # and not /media/
  MEDIA_ROOT = os.path.join(BASE_DIR, os.getenv("MEDIA_ROOT", "/medias/")) # From defaul os.path.join(BASE_DIR, "media")

STORAGES["staticfiles"] = STORAGES["default"] 

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATICFILES_FINDERS = [
  "django.contrib.staticfiles.finders.FileSystemFinder",
  "django.contrib.staticfiles.finders.AppDirectoriesFinder",
  "sass_processor.finders.CssFinder", # Ajouté
]

STATICFILES_DIRS = (
  os.path.join(PROJECT_DIR, "static"), # I suppose staticfiles are parsed to static
)

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles/") # static to staticfiles
STATIC_URL = "/static/" # Leading Slash optional?

# Django Sass
SASS_PROCESSOR_ROOT = os.path.join(BASE_DIR, "static/css") # check absent leading slash and static instead of staticfiles
SASS_PROCESSOR_AUTO_INCLUDE = False

# Wagtail settings

WAGTAIL_SITE_NAME = os.getenv("SITE_NAME", "Sites faciles")

# Search
# https://docs.wagtail.org/en/stable/topics/search/backends.html
WAGTAILSEARCH_BACKENDS = {
  "default": {
    "BACKEND": "wagtail.search.backends.database",
  }
}

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
WAGTAILADMIN_BASE_URL = f"{os.getenv('HOST_PROTO', 'https')}://{HOST_URL}"

HOST_PORT = os.getenv("HOST_PORT", "")
if HOST_PORT != "":
  WAGTAILADMIN_BASE_URL = f"{WAGTAILADMIN_BASE_URL}:{HOST_PORT}"

# Allowed file extensions for documents in the document library.
# This can be omitted to allow all files, but note that this may present a security risk
# if untrusted users are allowed to upload files -
# see https://docs.wagtail.org/en/stable/advanced_topics/deploying.html#user-uploaded-files
WAGTAILDOCS_EXTENSIONS = [
  "csv",
  "docx",
  "key",
  "odt",
  "pdf",
  "pptx",
  "rtf",
  "txt",
  "xlsx",
  "zip",
]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")
WAGTAILTRANSFER_SECRET_KEY = os.getenv("WAGTAILTRANSFER_SECRET_KEY")

WAGTAILTRANSFER_SOURCES = {}
for i in range(0, 3):
  if os.getenv("WAGTAILTRANSFER_%i_SECRET_KEY" % i):
    WAGTAILTRANSFER_SOURCES[os.getenv("WAGTAILTRANSFER_%i_NAME" % i)] = {
      "BASE_URL": os.getenv("WAGTAILTRANSFER_%i_BASE_URL" % i),
      "SECRET_KEY": os.getenv("WAGTAILTRANSFER_%i_SECRET_KEY" % i),
    }

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

# Disable Gravatar service
WAGTAIL_GRAVATAR_PROVIDER_URL = None

WAGTAIL_RICHTEXT_FIELD_FEATURES = [
  "h2",
  "h3",
  "h4",
  "bold",
  "italic",
  "link",
  "document-link",
  "image",
  "embed",
]

WAGTAILEMBEDS_RESPONSIVE_HTML = True
WAGTAIL_MODERATION_ENABLED = False
WAGTAILMENUS_FLAT_MENUS_HANDLE_CHOICES = (
  ("header_tools", "Menu en haut à droite"),
  ("footer", "Menu en pied de page"),
  ("mega_menu_section_1", "Catégorie de méga-menu 1"),
  ("mega_menu_section_2", "Catégorie de méga-menu 2"),
  ("mega_menu_section_3", "Catégorie de méga-menu 3"),
  ("mega_menu_section_4", "Catégorie de méga-menu 4"),
  ("mega_menu_section_5", "Catégorie de méga-menu 5"),
  ("mega_menu_section_6", "Catégorie de méga-menu 6"),
  ("mega_menu_section_7", "Catégorie de méga-menu 7"),
  ("mega_menu_section_8", "Catégorie de méga-menu 8"),
  ("mega_menu_section_9", "Catégorie de méga-menu 9"),
  ("mega_menu_section_10", "Catégorie de méga-menu 10"),
  ("mega_menu_section_11", "Catégorie de méga-menu 11"),
  ("mega_menu_section_12", "Catégorie de méga-menu 12"),
  ("mega_menu_section_13", "Catégorie de méga-menu 13"),
  ("mega_menu_section_14", "Catégorie de méga-menu 14"),
  ("mega_menu_section_15", "Catégorie de méga-menu 15"),
  ("mega_menu_section_16", "Catégorie de méga-menu 16"),
)

WAGTAILIMAGES_EXTENSIONS = ["gif", "jpg", "jpeg", "png", "webp", "svg"]

CSRF_TRUSTED_ORIGINS = []
for host in ALLOWED_HOSTS:
  CSRF_TRUSTED_ORIGINS.append("https://" + host)

SF_ALLOW_RAW_HTML_BLOCKS = os.getenv("SF_ALLOW_RAW_HTML_BLOCKS", "False").lower() == "true"

WAGTAILTRANSFER_UPDATE_RELATED_MODELS = [
  # "wagtail_village.contentpage",
  "wagtailimages.image",
]

WAGTAILTRANSFER_LOOKUP_FIELDS = {
  # "taggit.tag": ["slug"],
  # "wagtailcore.locale": ["language_code"],
  # "contenttypes.contenttype": ["app_label", "model"],
  "auth.permission": ["codename"],
  "auth.group": ["name"],
  "auth.user": ["username"],
  # "wagtail_village.ContentPage": ["locale", "slug", "content_type", "parent_id"],
}

# if DEBUG and "localhost" in HOST_URL:
if DEBUG_TOOLBAR:
  INTERNAL_IPS = [
    "127.0.0.1",
    "0.0.0.0",
  ]



from .base_local import *