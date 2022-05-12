from django.db import models
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField
from taggit.managers import TaggableManager
# Create your models here.
class ServiceModel(models.Model):
    id = models.AutoField
    title = models.CharField(max_length=500)
    desc = RichTextField()
    image = models.ImageField(upload_to='img/service/')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    slug = AutoSlugField(populate_from='title')
    add_time = models.DateTimeField(auto_now_add=True)
    seo_desc =  models.TextField(default=desc, max_length=50)
    tags = TaggableManager()
    seo_keywords = models.TextField(default=tags)
    class Meta:
        verbose_name_plural = 'Xizmatlar'
        
    def __str__(self):
        return self.title