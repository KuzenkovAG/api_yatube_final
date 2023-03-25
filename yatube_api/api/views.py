from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import filters, generics, permissions, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from . import serializers
from .permissions import IsAuthorOrReadOnly
from posts.models import Post, Group

User = get_user_model()


class PostViewSet(viewsets.ModelViewSet):
    """ViewSet for Post."""
    serializer_class = serializers.PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for Group."""
    serializer_class = serializers.GroupSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = Group.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    """ViewSet for Comment."""
    serializer_class = serializers.CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly,)

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        return post.comments.all()

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post_id=self.kwargs.get('post_id')
        )


class FollowView(generics.ListCreateAPIView):
    """ViewSet for Follow."""
    serializer_class = serializers.FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        user = get_object_or_404(User, id=self.request.user.id)
        return user.publisher.all()

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
