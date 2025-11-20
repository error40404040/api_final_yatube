# api/urls.py (ИСПРАВЛЕННАЯ ВЕРСИЯ)
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router_v1 = DefaultRouter()
router_v1.register('posts', PostViewSet, basename='posts')
router_v1.register('groups', GroupViewSet, basename='groups')
router_v1.register('follow', FollowViewSet, basename='follow')

posts_router = routers.NestedSimpleRouter(
    router_v1, r'posts', lookup='post'
)
posts_router.register(
    r'comments', CommentViewSet, basename='post-comments'
)

urlpatterns = [
    path('', include(router_v1.urls)),
    path('', include(posts_router.urls)),
]
