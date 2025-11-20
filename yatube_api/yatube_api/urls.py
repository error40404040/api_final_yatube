# yatube_api/urls.py (ФИНАЛЬНАЯ ВЕРСИЯ)
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('api/v1/', include('djoser.urls')),

    # ИСПРАВЛЕНИЕ: Этот путь создаст правильные эндпоинты
    # /api/v1/jwt/create/, /api/v1/jwt/refresh/ и т.д.
    path('api/v1/', include('djoser.urls.jwt')),

    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
]
