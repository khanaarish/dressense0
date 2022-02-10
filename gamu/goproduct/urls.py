from django.urls import path

from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('<slug:category_slug>/<slug:product_slug>/',
         views.goproduct, name='goproduct'),
    path('<slug:category_slug>/', views.gocategory, name='gocategory')
]
