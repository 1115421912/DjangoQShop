from django.urls import path
from Buyer.views import *
urlpatterns = [
    path('login/', login),
    path('register/', register),
    path('index/', index),
    path('base/', base),
]