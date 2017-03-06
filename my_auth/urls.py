from django.conf.urls import url, include


urlpatterns = [
    url(r'^api/', include('my_auth.api.urls', namespace='my_auth_api')),
]
