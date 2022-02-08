from distutils.log import error
from django.shortcuts import render, redirect


from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from goproduct.models import Go_product


import http.client


from django.conf import settings
from django.views import View

from .models import Signup
import random
# Create your views here.


def home(request):
    return render(request, 'home.html')


def login(request):

    return render(request, 'login.html')


def goproduct(request):
    newest_products = Go_product.objects.all()[0:8]

    return render(request, 'goproduct.html', {'newest_products': newest_products})


def store(request):
    return render(request, 'store.html')


def bag(request):
    return render(request, 'bag.html')


def wishlist(request):
    return render(request, 'wishlist.html')


def account(request):
    return render(request, 'account.html')


class Coffee(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        postdata = request.POST
        name = postdata.get('name')
        email = postdata.get('email')
        phone = postdata.get('phone')
        password = postdata.get('password')

        value = {
            'name': name,
            'email': email,
            'phone': phone,
            'password': password
        }
        error_massage = None

        customer = Signup(name=name,
                          email=email,
                          phone=phone,
                          password=password)

        error_massage = self.validateSignup(customer)

        if not error_massage:
            print(name, phone, email, password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_massage,
                'values': value
            }
            return render(request, 'register.html', data)

    def validateSignup(self, customer):
        error_message = None
        if not customer.name:
            error_message = "First Name Required !!"
        elif len(customer.name) < 4:
            error_message = 'First Name must be 4 char long or more'
        elif not customer.phone:
            error_message = 'Phone Number required'
        elif len(customer.phone) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len(customer.password) < 6:
            error_message = 'Password must be 6 char long'
        elif len(customer.email) < 5:
            error_message = 'Email must be 5 char long'
        elif customer.isExists():
            error_message = 'Email Address Already Registered..'
        # saving

        return error_message


def cart(request):
    return render(request, 'cart.html')
