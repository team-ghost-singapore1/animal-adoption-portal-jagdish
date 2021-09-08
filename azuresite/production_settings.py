import os

# Import everything from the development_settings file
# Anything that is declared in both files will be overwritten by what is below
# more information is available here https://docs.djangoproject.com/en/3.2/topics/settings/
from .development_settings import *

# from azure.keyvault.secrets import SecretClient
# from azure.identity import DefaultAzureCredential


# # Start Key Vault
# keyVaultName = os.environ["Django__KeyVaultName"]
# KVUri = f"https://{keyVaultName}.vault.azure.net"

# credential = DefaultAzureCredential()
# client = SecretClient(vault_url=KVUri, credential=credential)

# # These string values should match the name of your secrets in the Key Vault
# django_secret_key = client.get_secret('DJANGO-SecretKey').value
# postgresql_username = client.get_secret('POSTGRESQL-Username').value
# postgresql_password = client.get_secret('POSTGRESQL-Password').value
# postgresql_host_name = client.get_secret('POSTGRESQL-HostName').value
# postgresql_database_name = client.get_secret('POSTGRESQL-DatabaseName').value
# # End Key Vault


# # Start debug mode
# DEBUG = True if "Django__Debug" in os.environ and os.environ["Django__Debug"] == "True" else False
# # End debug mode


# Configure the domain name using the environment variable
# that Azure automatically creates for us
# you can read more here https://docs.microsoft.com/en-us/azure/app-service/configure-language-python#production-settings-for-django-apps
ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []


# # Start secret key
# SECRET_KEY = django_secret_key
# # End secret key


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


# # Start Key Vault
# # Don't forget to remove the declaration above once you have integrated Key Vault
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': f'{postgresql_database_name}',
#         'USER': f'{postgresql_username}@{postgresql_host_name}',
#         'PASSWORD': f'{postgresql_password}',
#         'HOST': f'{postgresql_host_name}.postgres.database.azure.com',
#         'PORT': '5432',
#         'OPTIONS': {
#             'sslmode': 'require'
#         },
#     }
# }
# # End Key Vault


# Get these paths from the deployment logs
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = ('whitenoise.storage.CompressedManifestStaticFilesStorage')
