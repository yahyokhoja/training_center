"""
Django settings for training_center project with django-environ and PostgreSQL (Render + local support).
"""

import os
import socket
from pathlib import Path
import environ
from django.utils.translation import gettext_lazy as _

# =========================
# BASE_DIR
# =========================
BASE_DIR = Path(__file__).resolve().parent.parent

# =========================
# django-environ initialization
# =========================
env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))  # локальный .env

# =========================
# SECURITY
# =========================
SECRET_KEY = env('SECRET_KEY', default='changeme-in-production')
DEBUG = env('DEBUG', default=False)

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    'training-center-6j6m.onrender.com',
    '0.0.0.0',
]

# =========================
# Detect environment (local or Render)
# =========================
hostname = socket.gethostname()
IS_RENDER = 'render' in hostname.lower()

# =========================
# Database (PostgreSQL via .env)
# =========================
if IS_RENDER:
    # Render uses internal hostname
    POSTGRES_HOST = env('POSTGRES_HOST', default='dpg-d4041rre5dus7383jfp0-a')
else:
    # Local: use external hostname
    POSTGRES_HOST = env('POSTGRES_HOST', default='dpg-d4041rre5dus7383jfp0-a.oregon-postgres.render.com')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('POSTGRES_DB', default='training_center_db'),
        'USER': env('POSTGRES_USER', default='admin'),
        'PASSWORD': env('POSTGRES_PASSWORD', default='password'),
        'HOST': POSTGRES_HOST,
        'PORT': env('POSTGRES_PORT', default='5432'),
    }
}

# =========================
# Application definition
# =========================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'candidates',
    'employer',
    'Job',
    'main',
    'users',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'training_center.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'training_center.wsgi.application'

# =========================
# Password validation
# =========================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

AUTH_USER_MODEL = 'main.CustomUser'

LOGIN_URL = '/users/login/'
LOGIN_REDIRECT_URL = '/users/profile/'
LOGOUT_REDIRECT_URL = '/users/login/'

# =========================
# Internationalization
# =========================
LANGUAGE_CODE = 'ru'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

LANGUAGES = [
    ('ru', _('Russian')),
    ('en', _('English')),
    ('de', _('German')),
]

LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]

# =========================
# Static files
# =========================
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# =========================
# Default primary key field type
# =========================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
