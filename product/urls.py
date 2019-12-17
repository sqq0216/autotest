from django.urls import path

from . import views
#为url添加命名空间
app_name = 'product'
urlpatterns = [
    path('', views.index, name='index'),
    path('product_manage/',views.product_manage),
    
]
