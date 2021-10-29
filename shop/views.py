from django.core.checks import messages
from django.shortcuts import render, redirect

from django.urls import reverse

from django.http import HttpResponse, JsonResponse, request
from django.views import View

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

from .forms import AddImageForm, AddItemForm

from .models import Item, CartItem, Images

# Create your views here.


class Index(View):
    def get(self, req):

        cartcount = getCartCount(req.user)
        items = Item.objects.all()
        imgs = Images.objects.get(item=items[0])
        ctx = {
            'count': cartcount,
            'items': items,
            'img': imgs


        }

        return render(req, 'shop/home.html', ctx)


def Profile(req, pid):
    # form=UserChangeForm()
    items = Item.objects.filter(user=req.user)
    return render(req, 'shop/profile.html', {'items': items})


@login_required
def About(req):
    count = getCartCount(req.user)
    return render(req, 'shop/aboutus.html', {'count': count})


def Trending(req):
    count = getCartCount(req.user)
    return render(req, 'shop/trending.html', {'count': count})


def Products(req):
    count = getCartCount(req.user)
    items = Item.objects.all()
    return render(req, 'shop/products.html', {'count': count, 'items': items})


def NewItems(req):
    count = getCartCount(req.user)
    newitems = Item.objects.all()
    data = {
        'items': newitems,
        'count': count
    }
    return render(req, 'shop/newitems.html', data)


def Items(req, id):
    item = Item.objects.get(pk=id)
    count = getCartCount(req.user)
    data = {
        'item': item,
        'count': count
    }
    return render(req, 'shop/item.html', data)


class AddItem(View, LoginRequiredMixin):

    def get(self, req):
        itemform = AddItemForm()
        imageform = AddImageForm()
        count = getCartCount(req.user)
        ctx = {
            'itemform': itemform,
            'imageform': imageform,
            'count': count
        }
        return render(req, 'shop/additem.html', ctx)

    def post(self, req):
        itemform = AddItemForm(req.POST)
        imageform = AddImageForm(req.POST, req.FILES)

        if itemform.is_valid() and imageform.is_valid():

            item = itemform.save(commit=False)
            image = imageform.save(commit=False)
            item.user = req.user
            image.item = item
            item.save()
            image.save()

            return redirect('index')

        else:
            ctx = {
                'itemform': itemform,
                'imageform': imageform,
            }
            return render(req, 'shop/additem.html', ctx)


@login_required
def addtobasket(req, id):

    # print(id)
    previtem = Item.objects.get(pk=int(id))
    # print(previtem)
    # print(previtem)
    _, created = CartItem.objects.get_or_create(user=req.user, item=previtem)
    if not created:
        return JsonResponse({'data': False})
    else:

        # usercart=CartItem(user=req.user,item=previtem)
        # usercart.save()
        cartcount = getCartCount(req.user)

        data = {
            'data': True,
            'count': cartcount
        }
        print('created')
        return JsonResponse(data, status=200)


@login_required
def Cart(req, uid):
    if req.user.id != uid:
        return redirect('index')

    cart = CartItem.objects.filter(user_id=req.user.id)
    cartcount = len(cart)

    return render(req, 'shop/cart.html', {'cart': cart, 'count': cartcount})


@login_required
def RMCart(req, iID):

    item = CartItem.objects.get(pk=iID, user_id=req.user.id)
    item.delete()
    # print(item)

    return redirect('index')


@login_required
def BuyNow(req, id):

    try:
        item = CartItem.objects.get(pk=id)
    except Exception as e:
        return redirect('index')
    count = getCartCount(req.user)

    return render(req, 'shop/payment.html', {'item': item.item, 'count': count})


class EditItem(LoginRequiredMixin, View):

    def get(self, req, id):
        count = getCartCount(req.user)
        try:
            item = Item.objects.get(pk=id)
        except Exception as e:
            return redirect('index')

        if not item.user == req.user:
            return redirect('index')

        editform = AddItemForm(instance=item)

        data = {
            'form': editform,
            'count': count
        }

        return render(req, 'shop/edit.html', data)

    def post(self, req, id):
        item = Item.objects.get(pk=id)
        count = getCartCount(req.user)

        form = AddItemForm(req.POST)
        if form.is_valid() and not form.cleaned_data['price'] == 0:
            item.name = form.cleaned_data['name']
            item.price = form.cleaned_data['price']
            item.save()

            return redirect('index')
        else:
            return render(req, 'shop/edit.html', {'form': form, 'count': count})


def getCartCount(user):
    cart = CartItem.objects.filter(user_id=user.id)
    cartcount = len(cart)
    return cartcount
