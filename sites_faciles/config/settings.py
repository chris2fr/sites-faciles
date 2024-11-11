"""
Django settings for sites_faciles project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/

Inspiration
https://github.com/betagouv/tous-a-bord/blob/main/config/settings.py
"""

import os
from pathlib import Path

import dj_database_url
from dotenv import load_dotenv


# Prendre les variables d'environnement
load_dotenv()
# Check to see if basic variables needed are defined
REQUIRED = ["DBURL", "SECRET_KEY", "APP_DJANGO_ROOT"]
needs_required = []
for i in REQUIRED:
    if not os.getenv(i) != "":
        needs_required.append(i)
if needs_required != []:
    raise ValueError("Merci de mettre les variables suivantes dans .env: %s" % ", ".join(needs_required))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.getenv("APP_DJANGO_ROOT", Path(__file__).resolve().parent.parent.parent)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

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

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DJANGO_DEBUG", "false").lower() == "true"
DEBUG_TOOLBAR = os.environ.get("DJANGO_DEBUG_TOOLBAR", "false").lower() == "true"

ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "127.0.0.1, localhost").replace(" ", "").split(",")

HOST_URL = os.getenv("DJANGO_HOST", "localhost")

# Sites Faciles and Wagtail Translation seem to need this parameter
SITE_ID = os.getenv("DJANGO_SITE_ID", 1)

# Application definition
INSTALLED_APPS = [
    "django_design_system",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "django.contrib.sessions",
    "django.contrib.staticfiles",
    "modelcluster",
    "sass_processor",
    "search",
    "sites_faciles",
    "storages",
    "taggit",
    "wagtail",
    "wagtail_design_system",
    "wagtail_localize.locales",
    "wagtail_localize",
    "wagtail_transfer",
    "wagtail.admin",
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.contrib.settings",
    "wagtail.documents",
    "wagtail.embeds",
    "wagtail.images",
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
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]

# if DEBUG and "localhost" in HOST_URL:
if DEBUG_TOOLBAR:
    MIDDLEWARE += [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
    ]

ROOT_URLCONF = "sites_faciles.config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "django_design_system/templates"),
            os.path.join(BASE_DIR, "django_design_system/theme_design_system/templates"),
            os.path.join(BASE_DIR, "django_design_system/theme_lesgrandsvoisins/templates"),
            os.path.join(BASE_DIR, "sites_faciles/templates"),
            os.path.join(BASE_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "wagtail.contrib.settings.context_processors.settings",
                "wagtailmenus.context_processors.wagtailmenus",
                "django_design_system.context_processors.site_config",
                "wagtail_design_system.context_processors.skiplinks",
                "wagtail_design_system.context_processors.mega_menus",
                "wagtail_design_system.context_processors.urlangs",
                "wagtail_design_system.context_processors.sitevars",
            ],
        },
    },
]

WSGI_APPLICATION = "sites_faciles.config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASE_URL = os.getenv("DBURL")
print(DATABASE_URL)
if DATABASE_URL != "":
    DATABASES = {
        "default": dj_database_url.parse(
            DATABASE_URL,
            conn_max_age=600,
            conn_health_checks=True,
        )
    }
else:
    raise ValueError("Please set the DBURL environment variable")

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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

WAGTAIL_PASSWORD_RESET_ENABLED = os.getenv("WAGTAIL_PASSWORD_RESET_ENABLED", False).lower() == "true"


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "fr"

TIME_ZONE = "Europe/Paris"

USE_I18N = True

USE_L10N = True

USE_TZ = True

WAGTAIL_I18N_ENABLED = True

WAGTAIL_CONTENT_LANGUAGES = LANGUAGES = [
    ("en", "English"),
    ("fr", "French"),
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
STORAGES = {}
STORAGES["staticfiles"] = {
    "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
}

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "sass_processor.finders.CssFinder",
]

# S3 uploads & MEDIA CONFIGURATION
# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html

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
    STORAGES["default"] = {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    }
    MEDIA_URL = os.getenv("DJANGO_MEDIA_URL", "media/")
    MEDIA_ROOT = os.getenv("DJANGO_MEDIA_ROOT", os.path.join(BASE_DIR, "/mediafiles"))

# Django Sass
SASS_PROCESSOR_ROOT = os.path.join(BASE_DIR, "static/css")
SASS_PROCESSOR_AUTO_INCLUDE = False

STATIC_URL = os.getenv("DJANGO_STATIC_URL", "static/")
STATIC_ROOT = os.getenv("DJANGO_STATIC_ROOT", os.path.join(BASE_DIR, "/staticfiles"))

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "django_design_system/static"),
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

# Wagtail settings
# https://docs.wagtail.org/en/stable/reference/settings.html

WAGTAIL_SITE_NAME = os.getenv("APP_SITE_NAME", "Sites faciles")

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
WAGTAILADMIN_BASE_URL = "%s://%s" % (
    os.getenv("APP_HOST_PROTO", "https"),
    os.getenv("APP_HOST_DOMAIN", "0.0.0.0"),
)

HOST_PORT = os.getenv("APP_HOST_PORT", "443")
if HOST_PORT != "":
    WAGTAILADMIN_BASE_URL = "%s:%s" % (WAGTAILADMIN_BASE_URL, HOST_PORT)

# WAGTAILADMIN_BASE_URL = "http://0.0.0.0"

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
    CSRF_TRUSTED_ORIGINS.append(
        os.getenv("APP_HOST_PROTO", "http") + "://" + host + ":" + os.getenv("APP_HOST_PORT", "8000")
    )


print(CSRF_TRUSTED_ORIGINS)

SF_ALLOW_RAW_HTML_BLOCKS = os.getenv("SF_ALLOW_RAW_HTML_BLOCKS", "False").lower() == "true"

WAGTAILTRANSFER_UPDATE_RELATED_MODELS = [
    # "wagtail_design_system.contentpage",
    "wagtailimages.image",
]

WAGTAILTRANSFER_LOOKUP_FIELDS = {
    # "taggit.tag": ["slug"],
    # "wagtailcore.locale": ["language_code"],
    # "contenttypes.contenttype": ["app_label", "model"],
    "auth.permission": ["codename"],
    "auth.group": ["name"],
    "auth.user": ["username"],
    # "wagtail_design_system.ContentPage": ["locale", "slug", "content_type", "parent_id"],
}

# if DEBUG and "localhost" in HOST_URL:
if DEBUG_TOOLBAR:
    INTERNAL_IPS = [
        "127.0.0.1",
        "0.0.0.0",
    ]

# AUTHENTICATION_BACKENDS = (
#     # Needed to login by username in Django admin, regardless of `allauth`
#     "django.contrib.auth.backends.ModelBackend",
#     # `allauth` specific authentication methods, such as login by e-mail
#     "allauth.account.auth_backends.AuthenticationBackend",
# )

# SOCIALACCOUNT_PROVIDERS = {
#     "openid_connect": {
#         "OAUTH_PKCE_ENABLED": True,
#         # 'SOCIALACCOUNT_ONLY': True,
#         "APPS": [
#             {
#                 "provider_id": "key-lesgrandsvoisins-com",
#                 "name": "key.lesgrandsvoisins.com",
#                 "client_id": os.getenv("OPENID_NAME"),
#                 "secret": os.getenv("OPENID_SECRET"),
#                 "settings": {
#                     "server_url": os.getenv("OPENID_URL"),
#                     # Optional token endpoint authentication method.
#                     # May be one of "client_secret_basic", "client_secret_post"
#                     # If omitted, a method from the the server's
#                     # token auth methods list is used
#                     "token_auth_method": "client_secret_post",
#                 },
#             },
#         ],
#     }
# }

# ACCOUNT_AUTHENTICATION_METHOD = "username"
# SOCIALACCOUNT_AUTO_SIGNUP = True
# ACCOUNT_EMAIL_VERIFICATION = "none"
# SOCIALACCOUNT_ONLY = True
# ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"