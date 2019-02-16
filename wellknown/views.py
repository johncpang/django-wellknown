from django.http import (
    HttpResponse,
    HttpResponseForbidden,
    HttpResponseNotFound,
)
from wellknown.models import Resource

try:
    from robots.views import rules_list
except ImportError:
    rules_list = None

def handle(request, path, *args, **kwargs):
    if request.method != 'GET':
        return HttpResponseForbidden('Only GET allowed.')

    try:
        r = Resource.objects.get(path=path)
        content = r.content
        content_type = r.content_type
    except Resource.DoesNotExist:
        return HttpResponseNotFound('Resource %s does not exist.' % path)

    return HttpResponse(content or '', content_type=content_type)

def crossdomain(request, *args, **kwargs):
    """ View that overrides /crossdomain.xml to
        handle as a well-known resource.
    """
    return handle(request, 'crossdomain.xml', *args, **kwargs)

def robots(request, *args, **kwargs):
    """ Handle /robots.txt as a well-known resource or
        pass off request to django-robots.
    """
    if rules_list:  # use django-robots if it is installed
        return rules_list(request, *args, **kwargs)
    return handle(request, 'robots.txt', *args, **kwargs)
