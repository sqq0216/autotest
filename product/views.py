# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from product.models import Product

def index(request):
    return HttpResponse("Hello, world. You're at the product index.")
def product_manage(request):
    username = request.session.get('user', '')
    product_list = Product.objects.all()
    return render(request,'product_manage.html',{'user':username,'products':product_list})