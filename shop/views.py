from django.shortcuts import render, redirect

from django.http import HttpResponse,JsonResponse
from django.views import View

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


from django.contrib.auth.models import User

from .forms import AddImageForm,AddItemForm

from .models import Item

# Create your views here.

from json import dumps

count=1

class Index(View):
    def get(self, req):

        items=Item.objects.all()
        ctx={
            'count':count,
            'items':items
            
        }
        
        
        

        
        return render(req, 'shop/home.html',ctx)


def Profile(req, pid):
    return render(req, 'shop/profile.html')

@login_required
def About(req):
    return render(req, 'shop/aboutus.html')


def Trending(req):
    return render(req, 'shop/trending.html')


def Products(req):
    return render(req, 'shop/products.html')


def NewItems(req):
    return render(req, 'shop/newitems.html')


def Items(req, id):
    return render(req, 'shop/item.html', {'id': id})


class AddItem(View,LoginRequiredMixin):
    
    def get(self, req):
        itemform=AddItemForm()
        imageform=AddImageForm()
        ctx={
            'itemform':itemform,
            'imageform':imageform,
        }
        return render(req, 'shop/additem.html',ctx)

    def post(self, req):
        itemform=AddItemForm(req.POST)
        imageform=AddImageForm(req.POST,req.FILES)

        if itemform.is_valid() and imageform.is_valid():
            
            item=itemform.save(commit=False)
            image=imageform.save(commit=False)
            item.user=req.user
            image.item=item
            item.save()
            image.save()

            return redirect('index')


        else:
            ctx={
                'itemform':itemform,
                'imageform':imageform,
            }
            return render(req, 'shop/additem.html',ctx)


        


def addtobasket(req, id):

    count=increment(id)
    
    data={
        'count':count
    }
    return JsonResponse(data,status=200)


def increment(precount):
    return precount+1