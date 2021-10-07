from django.shortcuts import render, redirect

from django.http import HttpResponse,JsonResponse
from django.views import View


from django.contrib.auth.models import User

# Create your views here.

from json import dumps

count=1

class Index(View):
    def get(self, req):

        
        return render(req, 'shop/home.html',{'count':count})


def Profile(req, pid):
    return render(req, 'shop/profile.html')


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


class AddItem(View):
    def get(self, req):
        return render(req, 'shop/additem.html')

    def post(self, req):
        return HttpResponse('posted')


def addtobasket(req, id):

    count=increment(id)
    
    data={
        'count':count
    }
    return JsonResponse(data,status=200)


def increment(precount):
    return precount+1