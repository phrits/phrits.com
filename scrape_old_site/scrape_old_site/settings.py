"""
Django settings for scrape_old_site project.
"""

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

# ****************
# High Level Stuff
DEBUG = True
STATIC_URL = 'static/'
ROOT_URLCONF = 'scrape_old_site.urls'
WSGI_APPLICATION = 'scrape_old_site.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ********
# SECURITY
SECRET_KEY = 'django-insecure-q2c@7g2p425697i@_xt!+=!ke-+glavybwe@f%jhfr0&41vr!t'
ALLOWED_HOSTS = []
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# **********************
# Application definition
INSTALLED_APPS = [
    'Scrape.apps.ScrapeConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

# ********************
# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'EST5EDT'
USE_I18N = True
USE_TZ = True
