from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from my_auth.api.serializers import MyUserSerializer
from my_auth.models import MyUser


class MyUserListView(generics.ListAPIView):
    serializer_class = MyUserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        users = MyUser.objects.all()
        return users
