"""
Django settings for e_commerce_backend project.

Generated by 'django-admin startproject' using Django 5.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os
import dj_database_url  

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'e_commerce_backend.settings')
# django.setup()


from datetime import timedelta
from pathlib import Path
import environ
env = environ.Env()
environ.Env.read_env()
import os 


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

from decouple import config

SECRET_KEY = config('SECRET_KEY')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

CUSTOM_APPS = [
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    
]

# Project related apps

PROJECT_APPS = [
    'user',
    'cart',
    'cart_item',
    'order_items',
    'orders',
    'product',
    'product_category',
    'product_customize',
    
]


# Django By Default apps 
DJANGO_DEFAULT_APPS = [
    "django.contrib.admin",          # Admin app
    "django.contrib.auth",           # Auth app
    "django.contrib.contenttypes",   # ContentType app
    "django.contrib.sessions",       # Sessions app
    "django.contrib.messages",       # Messages app
    "django.contrib.staticfiles",    # Static files app
]



INSTALLED_APPS = DJANGO_DEFAULT_APPS + PROJECT_APPS + CUSTOM_APPS 



MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "e_commerce_backend.urls"

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

WSGI_APPLICATION = "e_commerce_backend.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases


# Here using sqlite3 

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }


# here using postgresql 


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': config('DB_NAME'),
#         'USER': config('DB_USER'),
#         'PASSWORD': config('DB_PASSWORD'),
#         'HOST': config('DB_HOST'),
#         'PORT': config('DB_PORT', default='5432'),  # Default to 5432 if not specified
#     }
# }

DATABASES = {
    'default': dj_database_url.parse(
        os.environ.get('DATABASE_URL')
    )
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"
MEDIA_URL ='media/'
# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"



REST_FRAMEWORK = {
    
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),

}

# JWT settings configuration

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=10),  # Shorter lifetime for security
    "REFRESH_TOKEN_LIFETIME": timedelta(days=15),  # 15 day refresh token lifetime
    "ROTATE_REFRESH_TOKENS": True,  # Enable rotation for better security
    "BLACKLIST_AFTER_ROTATION": True,  # Blacklist old refresh tokens after rotation
    "ALGORITHM": "HS256",  # Standard algorithm
    "AUTH_HEADER_TYPES": ("Bearer",),  # Standard header type
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_USER_CLASS": "user.User",  # Custom user model
}

AUTH_USER_MODEL = 'user.User'