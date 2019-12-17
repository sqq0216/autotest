# python web 开发过程（django开发入门）
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
4. 创建后端(默认开启的某些应用需要至少一个数据表，所以，在使用他们之前需要在数据库中创建一些表。)
   - python manage.py makemigrations
   - python manage.py migrate
   - python manage.py createsuperuser(创建超级用户)
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
 # 自动化平台开发
 ## 登录和退出功能
 在views中添加逻辑代码，并在template下创建html文件，然后在url中添加映射，即可
 ## 产品管理

 ## 接口自动化
 1. models：通过models.foreignkey与产品关联
 2. django.contrib.admin--管理admin界面的数据模型，通过编写model文件定义数据库表，然后在admin中进行注册（admin.site.register()）之后就可以在admin首页看到相应的数据表。
 3. 管理页面可以通过admin进行自定义，显示指定的数据（不会把数据库中的数据项全部显示出来）
     - 表单：field（'',''）--也可以嵌套：field（[‘’，{field('','')}], []）————控制add界面里的标签显示
     - 内联显示：将其中一个类内联到另一个里面
     - 列表显示（list_display)：————控制清单界面的显示（每一列的列头）
 ## BUG管理
 1. 设计数据库models，
 2. admin自定义表单
 3. setting 注册新的bug应用
 ## 系统设置（同bug管理）
 未实现
 ##   