from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, related_name='post_author', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    tags = TaggableManager()
    image = models.ImageField(upload_to='post/')
    created_at = models.DateTimeField(default=timezone.now)
    description = models.TextField(max_length=15000)
    category = models.ForeignKey('Category', related_name='post_category', on_delete=models.CASCADE)
    slug = models.SlugField(null=True, blank=True)


    def save(self, *args, **Kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **Kwargs)
    
    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"slug": self.slug})
    
   
    
    def __str__(self):
        return self.title
  

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
