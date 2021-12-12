import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_news_app.settings')

app = Celery('api_news_app')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'reseting-upvotes': {
        'task': 'news_board.tasks.reset_upvotes',
        'schedule': 60.0,
    }
}
