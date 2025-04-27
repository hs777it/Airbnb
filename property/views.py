from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Property


# Class Based View

class PropertyList(ListView):
    model = Property
    ## filter
    ## pagination

class PropertyDetail(DetailView):
    model = Property
    ## Booking   
    
