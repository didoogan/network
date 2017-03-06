from django.conf.urls import url, include

from . import views


urlpatterns = [
    url(r'^my_user_list/', views.MyUserListView.as_view(), name='my_user_list'),
]
