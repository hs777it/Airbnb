from django.contrib import admin
from .models import Link, SiteInfo
from django_summernote.admin import SummernoteModelAdmin


# Apply summernote to all TextField in model.
class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'


class MyModelAdmin(SomeModelAdmin): #admin.ModelAdmin
    def has_add_permission(self, request):
        return False

class NoAddNoDelete(SomeModelAdmin): # admin.ModelAdmin
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False

# add to project/wsgi.py
def once_time():
    if SiteInfo.objects.count() < 1:
        SiteInfo.objects.create_site_info("Airbnb Website","01033883434")


admin.site.register(SiteInfo,NoAddNoDelete)
admin.site.register(Link)