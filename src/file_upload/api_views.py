from django.contrib.auth import get_user_model

from rest_framework import viewsets, permissions, status, parsers, renderers

from drf_yasg.utils import swagger_auto_schema

from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, TokenVerifyView)

from .serializers import (
    UserSerializer,
    TokenObtainPairResponseSerializer,
    TokenVerifyResponseSerializer,
    TokenRefreshResponseSerializer,
    FileUploadSerializer,
    FileResultSerializer,
)
from .models import UploadedFile
from .services.mixins import MixedSerializer



class UserBaseViewSet(viewsets.ModelViewSet):
    """
    Base class
    """
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserRegistrationViewSet(UserBaseViewSet):
    """
    Registration
    """
    permission_classes = (permissions.AllowAny,)


class UserListViewSet(UserBaseViewSet):
    """
    User list
    """


class DecoratedTokenObtainPairView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: TokenObtainPairResponseSerializer})
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class DecoratedTokenVerifyView(TokenVerifyView):
    permission_classes = (permissions.AllowAny,)

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: TokenVerifyResponseSerializer})
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class DecoratedTokenRefreshView(TokenRefreshView):
    permission_classes = (permissions.AllowAny,)

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: TokenRefreshResponseSerializer})
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class FileUploadViewSet(viewsets.ModelViewSet):
    """
    2222222
    """
    queryset = UploadedFile.objects.all()
    serializer_class = FileUploadSerializer
    parser_classes = (parsers.MultiPartParser, )

    # serializer_classes_by_action = {
    #         # 'create': FileUploadSerializer,
    #         # 'list': FileUploadSerializer,
    #         'retrieve': FileResultSerializer
    #     }


class FileResultViewSet(viewsets.ModelViewSet):
    """
    333333
    """
    queryset = UploadedFile.objects.all()
    serializer_class = FileResultSerializer
