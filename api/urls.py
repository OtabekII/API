from . import views 
from django.urls import path

urlpatterns = [ 
    path('banner/list/', views.banner_list), 
    path('banner/detail/<int:id>/', views.banner_detail), 
    path('contact/list/', views.contact_list), 
    path('contact/detail/<int:id>/', views.contact_detail), 
    path('product/list/', views.product_list), 
    path('product/detail/<int:id>/', views.product_detail), 
    path('category/list/', views.category_list), 
    path('category/detail/<int:id>/', views.category_detail),
]