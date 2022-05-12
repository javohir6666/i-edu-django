from django.db import models
from autoslug import AutoSlugField
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
# Create your models here.
class PageModel(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField()
    slug = slug = AutoSlugField(populate_from='title')
    tags = TaggableManager()
    seo_desc = models.CharField(default=description, max_length=100)
    seo_keywords = models.CharField(default=tags, max_length=100)
    add_time = models.DateTimeField(auto_now_add=True)
    class Meta:
            verbose_name_plural = 'Sahifalar'
        
    def __str__(self):
        return self.title