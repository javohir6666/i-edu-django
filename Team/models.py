from django.conf import settings
from django.db import models
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField
from taggit.managers import TaggableManager
# Create your models here.
class TeamCategory(models.Model):
    title = models.CharField(max_length=50)
    desc = RichTextField()
    slug = AutoSlugField(populate_from='title')
    add_time = models.DateTimeField(auto_now_add=True)
    seo_desc =  models.TextField(default='desc', max_length=50)
    tags = TaggableManager()
    seo_keywords = models.TextField(default=tags)
    
    class Meta:
        verbose_name_plural = 'Lavozimlar'
        
    def __str__(self):
        return self.title

class Worker(models.Model):
    id = models.AutoField
    position = models.ForeignKey(TeamCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    image = models.ImageField(upload_to='img/')
    desc = RichTextField()
    email=models.EmailField(max_length=200)
    twitter = models.URLField(max_length=250,null=True)
    instagram = models.URLField(max_length=250,null=True)
    facebook = models.URLField(max_length=250,null=True)
    linkedin = models.URLField(max_length=250,null=True)
    telegram = models.URLField(max_length=250,null=True)
    profile = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    add_time = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='name')
    class Meta:
        verbose_name_plural = 'Ishchilar'
        
    def __str__(self):
        return self.name