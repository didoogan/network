from django.conf import settings
from django_rq import job

import clearbit



@job
def get_user_info(user):
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! in get_user_info() !!!!!!!!!!!!!!!!!!!')
    clearbit.key = settings.CLEARBIT_SECRET_KEY
    person = clearbit.Person.find(email=user.email, stream=True)
    if person:
        print(person)
