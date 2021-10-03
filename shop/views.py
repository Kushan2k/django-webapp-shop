from django.shortcuts import render

from django.http import HttpResponse
from django.views import View

# Create your views here.


class Index(View):
    def get(self, req):
        return render(req, 'shop/home.html', {'numbers': [1, 2, 3, 4, 5, 6, 7, 8, 9]})


def About(req):
    return render(req, 'shop/aboutus.html')


def Trending(req):
    return render(req, 'shop/trending.html')


def Products(req):
    return render(req, 'shop/products.html')


def NewItems(req):
    return render(req, 'shop/newitems.html')


def Item(req, id):
    return render(req, 'shop/item.html', {'id': id})
