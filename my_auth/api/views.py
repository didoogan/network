import requests
import clearbit
import django_rq

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status

from django.conf import settings
from django.contrib.auth import get_user_model

from django_rq import job

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
        if result.status_code != 200:
            return Response({'error': 'API error'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        result_status = result.json()['data']['result']
        if result_status != 'deliverable':
            return Response({'error': 'Unappropriat email'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        CustomUser = get_user_model()
        u = CustomUser.objects.create(email=email)
        u.set_password(psw)
        u.save()
        get_user_info.delay(u)
        return Response({'message': 'Success'}, status=status.HTTP_201_CREATED)


@job
def get_user_info(user):
    print('in get_user_info()')
    clearbit.key = settings.CLEARBIT_SECRET_KEY
    person = clearbit.Enrichment.find(email=user.email, stream=True)
    if person is not None:
        print("Name: " + person['name']['fullName'])











