# TODO:  Напишите свой вариант
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (IsAuthenticatedOrReadOnly,
                                        IsAuthenticated)

from posts.models import Group, Post, User
from .serializers import (CommentSerializer, FollowSerializer,
                          GroupSerializer, PostSerializer)
from .permissions import OwnerOrRead


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, OwnerOrRead]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, OwnerOrRead]

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


@action(methods=['POST', 'GET'])
class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username', 'user__username')

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user.username)
        return user.follower

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
