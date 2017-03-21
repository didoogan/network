from django.db.models import Count
from django.db.models import Q
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response

from post.models import Post, Like
from utils.drf.paginators.paginators import PostPagination
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    pagination_class = PostPagination

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

    @detail_route(methods=['post'])
    def like(self, request, pk=None):
        user = request.user
        post = self.get_object()
        like, created = Like.objects.get_or_create(post=post, user=user)
        like.like = False if like.like else True
        like.save()
        serializer = PostSerializer(post)
        return Response({'post': serializer.data}, status=status.HTTP_201_CREATED)

    @detail_route(methods=['post'])
    def dislike(self, request, pk=None):
        user = request.user
        post = self.get_object()
        dislike, created = Like.objects.get_or_create(post=post, user=user)
        dislike.dislike = False if dislike.dislike else True
        dislike.save()
        serializer = PostSerializer(post)
        return Response({'post': serializer.data}, status=status.HTTP_201_CREATED)

    @list_route(methods=['get'])
    def get_max_posts_user(self, request, pk=None):
        post = Post.objects.all().annotate(num_likes=Count('like__like')).order_by('num_likes').last()
        return Response({'email': post.user.email}, status=status.HTTP_200_OK)

    @list_route(methods=['get'])
    def get_liking_posts(self, request, pk=None):
        p1 = Post.objects.filter(like__like=True)
        posts = Post.objects.filter(~Q(id__in=p1)).exclude(user=request.user)
        serializer = PostSerializer(posts, many=True)
        return Response({'posts': serializer.data}, status=status.HTTP_200_OK)






