import os

from celery import Celery

from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')


app = Celery(
    'config',
    broker='redis://file_upload_redis_server_container:6379',
    backend='redis://file_upload_redis_server_container:6379',
)


# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')


# Load task modules from all registered Django apps.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


# The debug_task dumps its own request information.
# bind=True task option to easily refer to the current task instance.
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
