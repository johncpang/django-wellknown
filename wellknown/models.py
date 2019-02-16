from django.db import models
import mimetypes

#
# resource model
#

class Resource(models.Model):
    path = models.CharField(max_length=128, unique=True)
    content = models.TextField(blank=True)
    content_type = models.CharField(max_length=128, blank=True)
    
    class Meta:
        ordering = ('path',)
    
    def __unicode__(self):
        return self.path
    
    def save(self, **kwargs):
        self.path = self.path.strip('/')
        if not self.content_type:
            self.content_type = mimetypes.guess_type(self.path)[0] or 'text/plain'
        super(Resource, self).save(**kwargs)
