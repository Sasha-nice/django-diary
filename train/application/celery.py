import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'application.settings')

app = Celery('application', include=['application.tasks'])

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'write_num_of_objects': {
        'task': 'application.tasks.add1',
        'schedule': 10,
        'args': (1, 2),
    }
}