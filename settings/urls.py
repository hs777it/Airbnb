from django.urls import path
from .views import contact_us, hello, home,home_search,category_filter


app_name = 'settings'

urlpatterns =[
    path("", home, name="home") ,  
    path("search", home_search, name="home_search"),
    path("contact_us", contact_us, name="contact_us"),
    path("category/<slug:category>", category_filter, name="category_filter"),
    
    
    path("hello",hello),
]


# Create Onec when visit url
#  SiteInfo.objects.create_site_info("Airbnb Website","01033883434")
