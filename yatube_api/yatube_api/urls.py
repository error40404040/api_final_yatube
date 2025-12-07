# yatube_api/urls.py

from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

# Импорт стандартной вьюхи для получения токена (нужно для pytest)
from rest_framework.authtoken import views

# Импорты для JWT (нужны для Postman)
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

# Импортируем наши кастомные сериализаторы (для исправления текстов ошибок в Postman)
from api.serializers import CustomTokenRefreshSerializer, CustomTokenVerifySerializer

urlpatterns = [
    path('admin/', admin.site.urls),

    # 1. Основные эндпоинты приложения (posts, groups, comments, follow)
    path('api/v1/', include('api.urls')),

    # 2. Управление пользователями (регистрация, получение списка и т.д.)
    path('api/v1/', include('djoser.urls')),

    # 3. Эндпоинт для получения стандартного токена (НЕ JWT).
    # Этот путь критически важен для прохождения старых тестов pytest.
    path('api/v1/api-token-auth/', views.obtain_auth_token),

    # 4. Переопределение JWT эндпоинтов для Postman.
    # Мы подставляем наши сериализаторы, чтобы возвращать ошибку "Token is invalid or expired".
    # ВАЖНО: Эти пути должны идти ПЕРЕД include('djoser.urls.jwt')
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

    # 5. Остальные JWT эндпоинты (включая создание токена /jwt/create/)
    path('api/v1/', include('djoser.urls.jwt')),

    # 6. Документация
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
]