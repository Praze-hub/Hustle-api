import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Create a Celery instance with the default Django settings module.
app = Celery('core')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
