from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework import status

from post.models import Post, Like
from post.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

    @detail_route(methods=['get'])
    def like(self, request, pk=None):
        user = request.user
        post = self.get_object()
        like, created = Like.objects.get_or_create(post=post, user=user)
        like.like = 0 if like.like else 1
        like.save()
        return Response({'status': 'Performed'}, status=status.HTTP_201_CREATED)

    @detail_route(methods=['get'])
    def unlike(self, request, pk=None):
        user = request.user
        post = self.get_object()
        unlike, created = Like.objects.get_or_create(post=post, user=user)
        unlike.unlike = 0 if unlike.unlike else 1
        unlike.save()
        return Response({'status': 'Performed'}, status=status.HTTP_201_CREATED)


