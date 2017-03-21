from django.conf.urls import url

from api.my_auth import views

urlpatterns = [
    url(r'^my_user_list/', views.MyUserListView.as_view(), name='my_user_list'),
    url(r'^signup/', views.SignUp.as_view(), name='signup'),
]
