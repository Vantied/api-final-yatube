from rest_framework import viewsets, permissions, filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.exceptions import PermissionDenied, ValidationError

from django.shortcuts import get_object_or_404

from posts.models import Post, Group, Follow
from .serializers import (
    PostSerializer, CommentSerializer, GroupSerializer, FollowSerializer)
from .permissions import IsAuthorOrReadOnly


class IsAuthorAndAuthenticated(viewsets.ModelViewSet):
    """
    Читать может любой, как авторизированный, так и аноним.
    Изменять или удалять могут только авторы.
    """
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly)


class PostViewSet(IsAuthorAndAuthenticated):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        if self.request.user.is_anonymous:
            raise PermissionDenied("Не авторизован")
        serializer.save(author=self.request.user)


class CommentViewSet(IsAuthorAndAuthenticated):
    serializer_class = CommentSerializer
    pagination_class = None

    def get_post(self):
        return get_object_or_404(Post, pk=self.kwargs['post_id'])

    def get_queryset(self):
        return self.get_post().comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_post())


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.AllowAny,)
    pagination_class = None


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)
    pagination_class = None
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        following_user = serializer.validated_data['following']
        if Follow.objects.filter(
            user=self.request.user, following=following_user
        ).exists():
            raise ValidationError("Вы уже подписаны на этого пользователя")
        serializer.save(user=self.request.user)
