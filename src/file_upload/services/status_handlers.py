from file_upload.models import UploadedFile


def set_next_status(instance: UploadedFile) -> None:
    status_iterator = iter(instance.PROCESSING_STATUSES)

    try:
        instance.status = next(status_iterator)[0]
    except StopIteration as e:
        print('The final file processing status has been reached')
    instance.save()
