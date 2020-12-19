from django.urls import path, re_path, register_converter
from . import views, converter

# 注册自定义过滤器，新建converter.py文件
register_converter(converter.InterConverter, 'IntYear')

urlpatterns = [
    # 传入空值进行分配url地址,分配至views.py的index方法
    path('', views.index),
    # 传入变量进行分配url地址,如果为int类型则分配至views.py的year方法，否则返回404
    # path('<int:year>', views.showInt),
    # 传入变量进行分配url地址,如果格式为int/str则分配至views.py的name方法，否则返回404
    path('<int:year>/<str:name>', views.showStr),
    # 正则表达式 导入re_path
    # re_path('(?P<year>[0,9]{4}.html',views.myyear,name='正则表达式'),
    # 提取正则表达式，自定义过滤器 导入register_converter
    path('<IntYear:year>', views.showInt),
    path('<str:name>', views.showOtherHtml),
]
