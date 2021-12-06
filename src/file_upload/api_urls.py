from django.urls import path
from . import api_views


urlpatterns = [
    path('auth/users/register/', api_views.UserRegistrationViewSet.as_view({'post': 'create'})),
    path('auth/users/list/', api_views.UserListViewSet.as_view({'get': 'list'})),
    path('auth/token/create', api_views.DecoratedTokenObtainPairView.as_view()),
    path('auth/token/verify/', api_views.DecoratedTokenVerifyView.as_view()),
    path('auth/token/refresh/', api_views.DecoratedTokenRefreshView.as_view()),
    path('file/upload/', api_views.FileUploadViewSet.as_view({'post': 'create'})),
    path('file/result/<int:pk>/', api_views.FileResultViewSet.as_view({'get': 'retrieve'})),
]
