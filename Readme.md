# pyhton web 开发过程（django开发入门）
## django简介
开发模式为MTV：  
- M 带包模型(Model) 负责业务对象和数据库的关系映射(ORM)
- T 代表模板(Template) 负责如何把页面展示给用户(html)
- V 代表视图 （View） 负责业务逻辑 并在适当时候调用Mode和Template
- 出了以上三层外，还需要一个URL分发器、他的作用是讲一个个URL的页面请求分发给不同的View处理，
## 开发过程
1. 搭建环境
   - python + django + mysql + navicat + pymysql库
2. 创建项目
   - django-admin startproject autotest（生成文件夹和manage.py）
3. 开启服务进行测试
   - python manage.py runserver（可以进行访问默认端口8000）
4. 创建后端
   - python manage.py makemigrations
   - python manage.py migrate
   - python manage.py createsuperuser
5. 创建应用
   - python manage.py startapp apitest
   - 在settings中添加app信息(注册应用程序)
6. 创建视图
   - 在view中加入test函数（实现函数功能）
7. 创建映射
   - url.py中添加新实现的函数，使其可以通过浏览器进行访问
8. 创建模板
   - template下新建login.py文件编写html
   - 在views中添加login函数
   - 在url.py中添加映射