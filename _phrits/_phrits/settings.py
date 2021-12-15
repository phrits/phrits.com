from pathlib import Path

# *****************************************************************************
# Basics
# *****************************************************************************
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_DIR = BASE_DIR
STATIC_URL = 'static/'
ROOT_URLCONF = '_phrits.urls'
WSGI_APPLICATION = '_phrits.wsgi.application'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# *****************************************************************************
# Security
# *****************************************************************************
SECRET_KEY = 'django-insecure-%9d16)yjo7q70ne=jna9dp!2j-lp@=qh-jpuz-_o@v8%p2=b+2'
CSRF_COOKIE_SECURE = True
DEBUG = True
ALLOWED_HOSTS = []
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# *****************************************************************************
# Applications
# *****************************************************************************
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'welcome.apps.WelcomeConfig',
]

# *****************************************************************************
# Middleware
# *****************************************************************************
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# *****************************************************************************
# Templates
# *****************************************************************************
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

# *****************************************************************************
# Database
# *****************************************************************************
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# *****************************************************************************
# Internationalization
# *****************************************************************************
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'EST5EDT'
USE_I18N = True
USE_TZ = True
