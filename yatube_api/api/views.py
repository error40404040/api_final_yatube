# api/views.py (ФИНАЛЬНАЯ ВЕРСИЯ)
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, filters, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination
from posts.models import Post, Group, Follow
from .permissions import IsAuthorOrReadOnly
from .serializers import (
    CommentSerializer, FollowSerializer, GroupSerializer, PostSerializer
)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    def get_queryset(self):
        # ИСПРАВЛЕНИЕ: Перенес длинную строку для PEP8
        post = get_object_or_404(
            Post, pk=self.kwargs.get('post_pk')
        )
        return post.comments.all()

    def perform_create(self, serializer):
        # ИСПРАВЛЕНИЕ: Перенес длинную строку для PEP8
        post = get_object_or_404(
            Post, pk=self.kwargs.get('post_pk')
        )
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.request.user.follower.all()
        return Follow.objects.none()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
