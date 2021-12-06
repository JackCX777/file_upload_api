from django.contrib.auth import get_user_model

from rest_framework import viewsets, permissions, status, parsers

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


class UserBaseViewSet(viewsets.ModelViewSet):
    """
    Base user viewset class
    """
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserRegistrationViewSet(UserBaseViewSet):
    """
    The user registration endpoint.
    """
    permission_classes = (permissions.AllowAny,)


class UserListViewSet(UserBaseViewSet):
    """
    The end point of the List of registered users .
    """


class DecoratedTokenObtainPairView(TokenObtainPairView):
    """
    The token creation endpoint.
    """
    permission_classes = (permissions.AllowAny,)

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: TokenObtainPairResponseSerializer})
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class DecoratedTokenVerifyView(TokenVerifyView):
    """
    The token verification endpoint.
    """
    permission_classes = (permissions.AllowAny,)

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: TokenVerifyResponseSerializer})
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class DecoratedTokenRefreshView(TokenRefreshView):
    """
    The token refresh endpoint.
    """
    permission_classes = (permissions.AllowAny,)

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: TokenRefreshResponseSerializer})
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class FileUploadViewSet(viewsets.ModelViewSet):
    """
    The file uploading endpoint.
    Accepts only *.xls or *.xlsx files.
    """
    queryset = UploadedFile.objects.all()
    serializer_class = FileUploadSerializer
    parser_classes = (parsers.MultiPartParser, )


class FileResultViewSet(viewsets.ModelViewSet):
    """
    The processing result endpoint.
    """
    queryset = UploadedFile.objects.all()
    serializer_class = FileResultSerializer
