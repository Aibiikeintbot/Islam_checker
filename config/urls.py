from django.contrib import admin
from django.core.cache import cache
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title='Islam Checker AI API',
        default_version='v1',
        description='API для проверки заданий студентов',
        contact=openapi.Contact(email='islamai@gmail.com'),

    ),
    public=True,
    permission_classes=[permissions.AllowAny],

)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('apps.users.urls')),
    path('api/submissions/', include('apps.submissions.urls')),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger_ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),
]


