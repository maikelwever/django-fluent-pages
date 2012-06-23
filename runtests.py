#!/usr/bin/env python

# Django environment setup:
from django.conf import settings
from django.core.management import call_command
from os.path import dirname, realpath
import sys

# Detect location and available modules
module_root = dirname(realpath(__file__))

# Inline settings file
settings.configure(
    DEBUG = True,
    TEMPLATE_DEBUG = True,
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:'
        }
    },
    TEMPLATE_LOADERS = (
        'django.template.loaders.app_directories.Loader',
    ),
    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sites',
        'fluent_pages',
        'fluent_pages.tests.testapp',
    ),
    SITE_ID = 4,
    ROOT_URLCONF = 'fluent_pages.tests.testapp.urls',
)

call_command('syncdb', verbosity=1, interactive=False)


# ---- app start

from django.test.utils import get_runner
TestRunner = get_runner(settings)  # DjangoTestSuiteRunner
runner = TestRunner(verbosity=1, interactive=True, failfast=False)
failures = runner.run_tests(['fluent_pages'])

if failures:
    sys.exit(bool(failures))