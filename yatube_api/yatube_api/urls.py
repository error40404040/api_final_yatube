# yatube_api/urls.py

from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

# Импорт стандартной вьюхи для получения токена
from rest_framework.authtoken import views

# Импорты для JWT 
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

# Импортируем кастомные сериализаторы 
from api.serializers import CustomTokenRefreshSerializer, CustomTokenVerifySerializer

urlpatterns = [
    path('admin/', admin.site.urls),

    # Основные эндпоинты приложения (posts, groups, comments, follow)
    path('api/v1/', include('api.urls')),

    # Управление пользователями (регистрация, получение списка и т.д.)
    path('api/v1/', include('djoser.urls')),

    # Эндпоинт для получения стандартного токена (НЕ JWT).
    path('api/v1/api-token-auth/', views.obtain_auth_token),

    # Переопределение JWT эндпоинтов для Postman.
    path(
        'api/v1/jwt/refresh/',
        TokenRefreshView.as_view(serializer_class=CustomTokenRefreshSerializer),
        name='token_refresh'
    ),
    path(
        'api/v1/jwt/verify/',
        TokenVerifyView.as_view(serializer_class=CustomTokenVerifySerializer),
        name='token_verify'
    ),

    # Остальные JWT эндпоинты 
    path('api/v1/', include('djoser.urls.jwt')),

    # Документация
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
]