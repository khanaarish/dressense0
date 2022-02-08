from django.contrib import admin
from django.urls import path
from nitro.views import *
from .views import Coffee


urlpatterns = [
    path('', home, name='homepage'),
    path('login', login),
    path('store', store),
    path('bag', bag),
    path('wishlist', wishlist),
    path('account', account),
    path('register', Coffee.as_view()),
    path('cart', cart),
    path('goproduct', goproduct),
]
