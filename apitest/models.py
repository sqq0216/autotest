from django.db import models
from product.models import Product
# Create your models here.
class Apitest(models.Model):
    Product = models.ForeignKey('product.Product', on_delete=models.CASCADE,null=True)
    apitestname = models.CharField('用例名称', max_length = 64)
    apitestdesc = models.CharField('用例描述', max_length = 64)
    apitester = models.CharField('测试负责人', max_length= 16)
    apitestresult = models.BooleanField('测试结果', max_length=1)
    created_time = models.DateTimeField('创建时间', auto_now= True)
    class Meta():
        verbose_name = '流程场景'
        verbose_name_plural = '流程场景接口'
        def __str__(self):
            return self.apitestname

class Apistep(models.Model):
    REQUEST_METHOD = (('get','get'),('post','post'),('put','put'),('delete','delete'),('patch','patch'))
    Apitest = models.ForeignKey('Apitest', on_delete=models.CASCADE)
    apiname = models.CharField('用例名称', max_length = 100 )
    apiurl = models.CharField('接口url', max_length = 200)
    apiparamvalue = models.CharField('接口参数和值', max_length = 800)
    apimethod = models.CharField(verbose_name='接口方法', choices = REQUEST_METHOD, default = 'get', max_length = 200,null=True)
    apiresult = models.CharField('接口预期结果', max_length = 200)
    apiresponse = models.CharField('响应数据', max_length = 5000, null=True)
    apistatus = models.BooleanField('测试结果')
    created_time = models.DateTimeField('创建时间', auto_now=True)
    Apistep = models.CharField('测试步骤',max_length=100, null=True)

    def __str__(self):
        return self.apiname

class Apis(models.Model):
    REQUEST_METHOD = (('0','get'),('1','post'),('2','put'),('3','delete'),('4','patch'))
    Product = models.ForeignKey('product.Product',on_delete = models.CASCADE,null = True)

    apiname = models.CharField('用例名称',max_length = 100)
    apiurl = models.CharField('接口URL', max_length= 200)
    apiparamvalue = models.CharField('接口参数和值', max_length=800)
    apimethod = models.CharField(verbose_name='接口方法', choices = REQUEST_METHOD, default = '0', max_length = 200,null=True)
    apiresult = models.CharField('接口预期结果', max_length = 200)
    apiresponse = models.CharField('响应数据', max_length = 5000, null=True)
    apistatus = models.BooleanField('测试结果')
    created_time = models.DateTimeField('创建时间', auto_now=True)    
    class Meta():
        verbose_name = '单一接口用例'
        verbose_name_plural = '单一接口用例'
        def __str__(self):
            return self.apiname 