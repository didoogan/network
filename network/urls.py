from django.conf.urls import url, include
from django.contrib import admin

from rest_framework_jwt.views import verify_jwt_token

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-verify/', verify_jwt_token),
    url(r'^my_auth/', include('my_auth.urls')),
    url(r'^post/', include('post.urls')),
    url(r'^django-rq/', include('django_rq.urls')),
]

# urlpatterns += patterns('',
#     url(r'^django-rq/', include('django_rq.urls')),
# )
