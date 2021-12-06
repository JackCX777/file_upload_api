from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="File upload API",
      default_version='v1',
      description="This API provides for uploading *.xls and *.xlsx files, some post-processing of these files "
                  "and getting the result of processing. The API also provides associated endpoints for registration, "
                  "user list retrieval, Bearer JSON Web Token retrieval, verification and refresh of this token.",
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny, ),
)

urlpatterns = [
   # fixing console warning message
   # path('swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(
      '^swagger(?P<format>\.json|\.yaml)$',
      schema_view.without_ui(cache_timeout=0),
      name='schema-json'
   ),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
