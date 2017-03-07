from rest_framework import generics

from post.models import Post
from post.serializers import PostSerializer


class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

