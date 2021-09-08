import os

# Import everything from the development_settings file
# Anything that is declared in both files will be overwritten by what is below
# more information is available here https://docs.djangoproject.com/en/3.2/topics/settings/
from .development_settings import *

# Configure the domain name using the environment variable
# that Azure automatically creates for us
# you can read more here https://docs.microsoft.com/en-us/azure/app-service/configure-language-python#production-settings-for-django-apps
ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",
    'adoptionsite.apps.AdoptionsiteConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Fill out the correct details here, but DO NOT commit them to source control
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'taa_portal',
        'USER': 'user@hostname',
        'PASSWORD': 'redacted',
        'HOST': '<hostname>.postgres.database.azure.com',
        'PORT': '5432',
        'OPTIONS': {
            'sslmode': 'require'
        },
    }
}
# Get these paths from the deployment logs
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = ('whitenoise.storage.CompressedManifestStaticFilesStorage')
