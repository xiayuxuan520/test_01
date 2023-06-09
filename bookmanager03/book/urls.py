from django.urls import path

from book.views import create_book, shop, register, json, method, res, set_cookie, get_cookie
from django.urls import converters
from django.urls.converters import register_converter
from book.views import set_session, get_session, login, LoginView, OrderView


# 1.定义转换器
class MobileConverter:
    # 验证数据的关键
    regex = '1[3-9]\d{9}'

    # 验证没有问题的数据给视图函数

    def to_python(self, value):
        return int(value)

    # 将匹配的结果用于反向解析传值时使用

    def to_url(self, value):
        return str(value)


# 2.注册转换器才能使用
# converter转换器类, type_name转换器名字
register_converter(MobileConverter, 'phone')

urlpatterns = [
    path('create/', create_book),
    # <转换器的名字：变量名> 转换器会对变量名进行正则验证
    path('<int:city_id>/<phone:mobile>', shop),
    path('register/', register),
    path('json/', json),
    path('method/', method),
    path('res/', res),
    path('set_cookie/', set_cookie),
    path('get_cookie/', get_cookie),
    path('set_session/', set_session),
    path('get_session/', get_session),
    path('login/', login),
    # 类视图
    path('163login/', LoginView.as_view()),
    path('order/', OrderView.as_view()),
]
