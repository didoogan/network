from django.conf.urls import url, include


urlpatterns = [
    url(r'^api/', include('api.my_auth.urls', namespace='my_auth_api')),
]
