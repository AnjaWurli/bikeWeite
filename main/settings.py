"""
Django settings for main project.

Generated by 'django-admin startproject' using Django 3.2.15.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
from typing import List

import environ
from email.utils import getaddresses

env = environ.Env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

READ_DOT_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", default=False)
if READ_DOT_ENV_FILE:
    # OS environment variables take precedence over variables from .env
    env.read_env(str(BASE_DIR / ".env"))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="django-insecure-+_fai#*zi53=1w^y6hdai0spid)bvw2&$p=o952urq(iha2}",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG", True)


if env.list("ALLOWED_HOSTS", default=[]):
    ALLOWED_HOSTS: List[str] = env.list("ALLOWED_HOSTS")

LOGIN_REDIRECT_URL = "index"
LOGOUT_REDIRECT_URL = "index"


SOCIAL_PROVIDERS = env.list("SOCIAL_PROVIDERS", default=[])

SOCIALACCOUNT_PROVIDERS = env.json("SOCIALACCOUNT_PROVIDERS", default={})

SITE_ID = 1

# Application definition

INSTALLED_APPS = [
    "bike_weite",
    "django_vite",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

DJANGO_VITE_ASSETS_PATH = BASE_DIR / "bike_weite/static/"

DJANGO_VITE_DEV_MODE = DEBUG

ADMINS = getaddresses(env.list("ADMINS", default=[]))

MANAGERS = getaddresses(env.list("MANAGERS", default=[]))

X_FRAME_OPTIONS = "SAMEORIGIN"


AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]

if SOCIALACCOUNT_PROVIDERS or 1:

    INSTALLED_APPS.extend(
        [
            "allauth",
            "allauth.account",
            "allauth.socialaccount",
            "allauth.socialaccount.providers.openid_connect",
        ]
    )
    AUTHENTICATION_BACKENDS.append(
        "allauth.account.auth_backends.AuthenticationBackend",
    )
    SOCIALACCOUNT_EMAIL_VERIFICATION = "none"
    ACCOUNT_LOGOUT_REDIRECT_URL = "index"
    ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = "index"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "main.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "main.wsgi.application"

# Email settings
SERVER_EMAIL = env("SERVER_EMAIL", default="no-reply@example.com")

EMAIL_CONFIG = env.email(
    "EMAIL_URL", default="consolemail://user:password@localhost:25"
)

vars().update(EMAIL_CONFIG)

EMAIL_SUBJECT_PREFIX = env("EMAIL_SUBJECT_PREFIX", default="")

DATABASES = {
    "default": env.db_url(
        "DATABASE_URL", default="sqlite:///%s/db.sqlite3" % BASE_DIR
    )
}

CACHES = {"default": env.cache(default="dummycache://")}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"

STATIC_ROOT = BASE_DIR / "staticfiles"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

if not DEBUG:
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

ADMIN_LOCATION = env("ADMIN_LOCATION", default="admin/")
