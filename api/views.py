from rest_framework.decorators import api_view 
from rest_framework.response import Response
 
 
from .serializers import BannerSerializer, ContactSerializer, ProductSerializer, CategorySerializer 
from main.models import Banner, Contact, Product, Category 
 
 
 
@api_view(['GET']) 
def banner_list(request): 
    banners = Banner.objects.all() 
    serializer_data = BannerSerializer(banners, many=True)  
    return Response(serializer_data.data) 
 
@api_view(['GET']) 
def banner_detail(request, id): 
    banner = Banner.objects.get(id=id) 
    ser_data = BannerSerializer(banner).data 
    return Response(ser_data) 
 
 
 
 
 
@api_view(['GET']) 
def contact_list(request): 
    contants = Contact.objects.all() 
    serializer_data = ContactSerializer(contants, many=True)  
    return Response(serializer_data.data) 
 
@api_view(['GET']) 
def contact_detail(request, id): 
    contact = Contact.objects.get(id=id) 
    con_data = ContactSerializer(contact).data 
    return Response(con_data) 
 
 
 
 
@api_view(['GET']) 
def product_list(request): 
    products = Product.objects.all() 
    serializer_data = ProductSerializer(products, many=True)  
    return Response(serializer_data.data) 
 
@api_view(['GET']) 
def product_detail(request, id): 
    product = Product.objects.get(id=id) 
    pro_data = ProductSerializer(product).data 
    return Response(pro_data) 
 
 
 
 
@api_view(['GET']) 
def category_list(request): 
    categorys = Category.objects.all() 
    serializer_data = CategorySerializer(categorys, many=True)  
    return Response(serializer_data.data) 
 
@api_view(['GET']) 
def category_detail(request, id): 
    category = Category.objects.get(id=id) 
    cat_data = CategorySerializer(category).data 
    return Response(cat_data)