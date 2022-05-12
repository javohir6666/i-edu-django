from django.db import models
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField
from taggit.managers import TaggableManager
# Create your models here.
class ProjectModel(models.Model):
    ProjectName = models.CharField(max_length=500)
    ProjectDesc = RichTextField()
    image = models.ImageField(upload_to='img/projects/')
    website = models.URLField(max_length=250)
    tags = TaggableManager()
    slug = AutoSlugField(populate_from='ProjectName')
    add_time = models.DateTimeField(auto_now_add=True)
    seo_desc =  models.TextField(default=ProjectDesc, max_length=50)
    seo_keywords = models.TextField(default=tags)
    def __str__(self):
        return self.ProjectName
    
    class Meta:
        verbose_name_plural = 'Proyektlar'