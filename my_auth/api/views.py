import json
import requests
import clearbit

from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from django.conf import settings

from my_auth.api.serializers import MyUserSerializer
from my_auth.models import MyUser

from validate_email import validate_email


class MyUserListView(generics.ListAPIView):
    serializer_class = MyUserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        users = MyUser.objects.all()
        return users


class SignUp(APIView):
    permission_classes = ()

    def post(self, request):
        email = request.data.get('email')
        psw = request.data.get('password')
        if len(psw) < 8 or not validate_email(email):
            return Response(
                {'error': 'Incorrect credentials data.'},
                 status=status.HTTP_406_NOT_ACCEPTABLE
            )
        result = requests.get("{}email={}&api_key={}".format(settings.HUNTER_EMAIL_VERIFICATOR_API_URL,
                                                             email,
                                                             settings.HUNTER_API_KEY))
        status = result.json()['data']['result']

        clearbit.key = settings.CLEARBIT_SECRET_KEY




