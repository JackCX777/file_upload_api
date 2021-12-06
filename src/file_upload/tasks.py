import os
from datetime import datetime
from time import sleep

from django.shortcuts import get_object_or_404
# from django.conf import settings
from django.utils import timezone

from celery import shared_task

# from file_upload.models import UploadedFile

# import services.processing as processing

from file_upload.services import processing
from file_upload.services.status_handlers import set_next_status


@shared_task
# def handle_file(file_path: str, obj_id: int):
def handle_file(obj_id):
    """
    Receives the processing result and writes it into the database
    """
    from file_upload.models import UploadedFile

    obj = UploadedFile.objects.get(id=obj_id)

    obj.set_next_status()

    result = processing.get_result(obj.file.path)

    obj.result = result
    obj.finish_date = timezone.now()
    obj.set_next_status()
