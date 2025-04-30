from django.contrib import admin

# Register your models here.
from .models import Link, SiteInfo


admin.site.register(SiteInfo)
admin.site.register(Link)

