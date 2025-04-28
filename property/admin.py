from django.contrib import admin

# Register your models here.
from .models import Property,PropertyBook,PropertyImages,PropertyReview,Place,Category
from django_summernote.admin import SummernoteModelAdmin


# Apply summernote to all TextField in model.
class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

admin.site.register(Property,SomeModelAdmin)
admin.site.register(PropertyBook)
admin.site.register(PropertyImages)
admin.site.register(PropertyReview)
admin.site.register(Place)
admin.site.register(Category)

