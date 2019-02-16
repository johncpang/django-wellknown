from django.conf.urls import url
from wellknown.views import handle, crossdomain, robots

urlpatterns = [
    url(r'^\.well-known/(?P<path>.*)', handle, name='wellknown'),
    url(r'^crossdomain\.xml$', crossdomain, name='crossdomain.xml'),
    url(r'^robots\.txt$', robots, name='robots.txt'),
]
