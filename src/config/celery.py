import os

from celery import Celery

from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')


# app = Celery('file_upload', broker=f'redis://{settings.REDIS_HOST}', backend=f'redis://{settings.REDIS_HOST}')

# app = Celery('file_upload')

# app = Celery('config')
# app.conf.broker_url = 'redis://file_upload_celery_container:6379/0'
# app = Celery('config', broker=f'redis://{settings.REDIS_HOST}', backend=f'redis://{settings.REDIS_HOST}')
# app = Celery('config', broker=f'redis://{settings.REDIS_HOST}')

app = Celery(
    # 'file_upload',
    # !!!!!!!!
    'config',
    # broker='redis://file_upload_redis_server_container:6379/0',
    # backend='redis://file_upload_redis_server_container:6379/0',
    # !!!!!!!!
    broker='redis://file_upload_redis_server_container:6379',
    backend='redis://file_upload_redis_server_container:6379',
)

# app = Celery('config', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')


# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')


# Load task modules from all registered Django apps.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
# app.autodiscover_tasks()


# The debug_task dumps its own request information.
# bind=True task option to easily refer to the current task instance.
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
