# cleaning_store/celery.py
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cleaning_store.settings')

app = Celery('cleaning_store')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
