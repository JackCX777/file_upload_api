import os

from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.conf import settings


class UploadedFile(models.Model):

    PROCESSING_STATUSES = (
        ('1', 'Uploaded'),
        ('2', 'Processing'),
        ('3', 'Done')
    )
    status_iterator = iter(PROCESSING_STATUSES)

    file = models.FileField(upload_to=settings.UPLOADS_DIR, unique=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, choices=PROCESSING_STATUSES, blank=False, default='1')
    finish_date = models.DateTimeField(blank=True, null=True)
    result = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ('upload_date', )
        verbose_name = 'Uploaded File'
        verbose_name_plural = 'Uploaded Files'

    def set_next_status(self):
        try:
            if self.status == '1':
                self.status = next(self.status_iterator)[0]
                self.status = next(self.status_iterator)[0]
            else:
                self.status = next(self.status_iterator)[0]
        except StopIteration as e:
            print('The final file processing status has been reached')

        self.save()
        # return self

    def __str__(self):
        return str(self.file)


# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'file_upload.settings')
