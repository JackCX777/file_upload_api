from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import UploadedFile
# from file_upload.services import processing


@receiver(signal=post_save, sender=UploadedFile)
def start_processing(sender, instance, created, raw, using, update_fields, **kwargs):
    from file_upload.tasks import handle_file

    if created:
        handle_file.delay(instance.id)
