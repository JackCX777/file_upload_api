from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.conf import settings

from rest_framework import serializers

from .models import UploadedFile
from .services.validators import UniqueFileValidator


class UserSerializer(serializers.ModelSerializer):
    """
    Answers serializer
    """

    class Meta:
        model = get_user_model()
        fields = ('username', 'password', )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        instance = get_user_model().objects.create_user(**validated_data)
        return instance


class TokenObtainPairResponseSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()


class TokenVerifyResponseSerializer(serializers.Serializer):
    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()


class TokenRefreshResponseSerializer(serializers.Serializer):
    access = serializers.CharField()

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()


class FileUploadSerializer(serializers.ModelSerializer):
    """
    Upload file
    """

    class Meta:
        model = UploadedFile
        fields = ('file', )
        extra_kwargs = {
            'file': {
                'validators': [
                    FileExtensionValidator(allowed_extensions=['xls', 'xlsx']),
                    UniqueFileValidator(settings.UPLOADS_PATH)
                ]
            }
        }

    # def create(self, validated_data):
    #     instance = super(FileUploadSerializer, self).create(validated_data)
    #     handle_file.delay()
    #     return instance


class FileResultSerializer(serializers.ModelSerializer):
    """
    Result file 11111
    """
    status = serializers.CharField(source='get_status_display')

    class Meta:
        model = UploadedFile
        fields = "__all__"

