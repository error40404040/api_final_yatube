# api/urls.py
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()
# Регистрируем посты
router.register('posts', PostViewSet, basename='posts')
# Регистрируем группы
router.register('groups', GroupViewSet, basename='groups')
# Регистрируем подписки
router.register('follow', FollowViewSet, basename='followers')

# регистрируем комменты С УЧЕТОМ post_id
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('', include(router.urls)),
]