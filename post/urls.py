from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^post_list_create/$', views.PostListCreateView.as_view()),
]
