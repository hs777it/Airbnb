from django.db import models

class SiteInfo(models.Model):   
    site_name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='settings/')
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    desciption = models.TextField(max_length=300)
    fb_link = models.URLField( max_length=200)
    twitter_link = models.URLField( max_length=200)
    instagram_link = models.URLField( max_length=200)
    address = models.CharField(max_length=100,default='cairo')
    
    class Meta:
        # verbose_name = "SiteInfo"
        verbose_name_plural = "SiteInfo"
        
    def __str__(self):
        return self.site_name
    
    
class Link(models.Model):
    text = models.CharField(max_length=50)
    link = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = "Link"

    
    def __str__(self):
        return self.titles
