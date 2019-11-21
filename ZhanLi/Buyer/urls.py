from django.urls import path, re_path
from Buyer.views import *
urlpatterns = [
    path('login/', login),
    path('register/', register),
    path('index/', index),
    path('base/', base),
    path('lt/', logo_out),
    path('sc/', shopping_cart),
    path('success/', success),

    path('aql_add/', aql_add),
    path('aql_del/', aql_del),

    path('search/', search),
    # path('goods_info/', goods_info),
    re_path('goods_info/(?P<id>\d+)', goods_info),
]