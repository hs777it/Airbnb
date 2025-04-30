from django.urls import path
from . import views 

app_name = 'blog'

urlpatterns = [
    path('', views.PostList.as_view(),name='post_list'),
    path('<slug:slug>', views.PostDetail.as_view(),name='post_detail'),
    
    path('category/<slug:slug>', views.PostsByCategory.as_view(),name='post_by_category'),
    # path('category/<str:slug>', views.PostsByCategory.as_view(),name='post_by_category'),
    path('tags/<slug:slug>', views.PostsByTags.as_view(),name='post_by_tags'),
]

