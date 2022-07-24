
from __future__ import absolute_import
import os
from celery import Celery

from config.settings import INSTALLED_APPS


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')


app = Celery("parser_app")


app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks(lambda: INSTALLED_APPS)