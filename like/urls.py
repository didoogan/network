from django.conf.urls import url
from .import views


urlpatterns = [
    url(r'^(?P<post_pk>[0-9]+)/(?P<like>\blike\b|\bunlike\b)/$', views.create_update_like, name='create_update_like'),
]
