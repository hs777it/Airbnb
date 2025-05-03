from django.contrib import admin

from settings.admin import SomeModelAdmin
from .models import About,FAQ


admin.site.register(About,SomeModelAdmin)
admin.site.register(FAQ)