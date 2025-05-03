
import django
from django.shortcuts import redirect, render
from property.models import Place, Property,Category
from django.db.models.query_utils import Q
from django.db.models import Count
from blog.models import Post
from django.contrib.auth.models import User

def home(request):
    places = Place.objects.all().annotate(property_count=Count('property_place'))
    category = Category.objects.all()
    
    restaurant_list = Property.objects.filter(category__name = 'Restaurant')[:5]
    hotels_list = Property.objects.filter(category__name = 'Hotels')[:4]
    places_list = Property.objects.filter(category__name = 'Places')[:4]
    
    recent_posts = Post.objects.all()[:4]
    
    user_count = User.objects.all().count()
    place_count = Property.objects.filter(category__name = 'Places').count()
    restaurant_count = Property.objects.filter(category__name = 'Restaurant').count()
    hotels_count = Property.objects.filter(category__name = 'Places').count()
    
    return render(request, 'settings/home.html',{
        'places': places,
        'category': category,
        'restaurant_list': restaurant_list,
        'hotels_list': hotels_list,
        'places_list': places_list,
        'recent_posts':recent_posts,
        'user_count':user_count,
        'place_count':place_count,
        'restaurant_count':restaurant_count,
        'hotels_count':hotels_count,
    })

def home_search(request):
    name = request.GET.get('name')
    place = request.GET.get('place')
    
    property_list = Property.objects.filter(
         Q(name__icontains=name) &
         Q(place__name__icontains = place)
    )
    
    return render(request,"settings/home_search.html",{"property_list":property_list})

def category_filter(request,category):
    category = Category.objects.get(name=category)
    property_list = Property.objects.filter(category = category)
    return render(request,"settings/home_search.html",{"property_list":property_list})

def contact_us(request):
    pass


def hello(request):
    return redirect('property/')