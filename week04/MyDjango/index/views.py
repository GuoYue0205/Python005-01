from django.shortcuts import render,redirect
from django.http import HttpResponse


def index(request):
    return HttpResponse('hello world')


def showInt(request, year):
    return HttpResponse(f'I am Int {year}')


def showStr(request, **kwargs):
    return HttpResponse(kwargs['name'])


# 参数name名字必须和urls当中的path('<str:name>', views.showOtherHtml)保持一致
def showOtherHtml(request, name):
    # 使用templates当中的html文件作为展示页面,实质上是将view试图与模版进行绑定
    return render(request, 'abc.html')
    # 重定向到另外一个html地址，一般用在用户名密码登录之后的跳转
    # return redirect('/2020.html')
