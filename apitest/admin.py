from django.contrib import admin
from apitest.models import Apitest, Apistep, Apis
from product.models import Product
# Register your models here.


# 内联显示，继承admin.tabularinline
class ApistepAdmin(admin.TabularInline):
    list_display = ['apiname','apiurl','apiparamvalue','apimethod','apiresult','apistatus','created_time','id','apitest']
    model = Apistep
    extra = 1

class ApitestAdmin(admin.ModelAdmin):
    search_fields = ('apitestname',)#增加搜索框
    list_display = ['apitestname','apitester','apitestresult','created_time','id']
    inlines = [ApistepAdmin] # 将apistep内联到apitest中

class ApisAdmin(admin.ModelAdmin):
    list_display = ['apiname', 'apimethod','created_time','id']
    
admin.site.register(Apitest, ApitestAdmin)
admin.site.register(Apis,ApisAdmin)# 该类继承admin.TabularInline时无法进行注册，即admin.site.register(Apis,ApisAdmin)报错