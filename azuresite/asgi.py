"""
ASGI config for azuresite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# WEBSITE_HOSTNAME is a special environment variable set by Azure,
# you can read more here https://docs.microsoft.com/en-us/azure/app-service/configure-language-python#production-settings-for-django-apps
settings_module = 'azuresite.production_settings' if 'WEBSITE_HOSTNAME' in os.environ else 'azuresite.development_settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_asgi_application()
