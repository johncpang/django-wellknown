from django.conf.urls import include, url
from wellknown import urls
urlpatterns = [
    url(r'^', include(urls)),
]
