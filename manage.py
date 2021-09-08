#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    # WEBSITE_HOSTNAME is a special environment variable set by Azure,
    # you can read more here https://docs.microsoft.com/en-us/azure/app-service/configure-language-python#production-settings-for-django-apps
    settings_module = 'azuresite.production_settings' if 'WEBSITE_HOSTNAME' in os.environ else 'azuresite.development_settings'
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
