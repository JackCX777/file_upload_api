from django.utils import timezone

from celery import shared_task

from file_upload.services import processing


@shared_task
def handle_file(obj_id: int) -> None:
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
