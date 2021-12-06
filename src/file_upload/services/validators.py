from pathlib import Path, PosixPath

from django.core.files.uploadedfile import InMemoryUploadedFile

from rest_framework import serializers

from file_upload.models import UploadedFile


class UniqueFileValidator:
    """
    Custom validator checks if the file has already been uploaded.
    """
    def __init__(self, uploads_dir_path: PosixPath):
        self.uploads_dir_path = uploads_dir_path

    def __call__(self, file: InMemoryUploadedFile) -> None:
        file = Path(self.uploads_dir_path / file.name)
        # print('!!!!!!!!!!!!!!!!!', file.path, type(file.path))

        # if file.is_file() or UploadedFile.objects.filter(file=file.path).exists():
        if file.is_file():
            message = f'A file named {file.name} has already been uploaded.'
            raise serializers.ValidationError(message)
