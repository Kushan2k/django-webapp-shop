from django.shortcuts import render, redirect
from django.views import View
from . import forms

# Create your views here.


class Login(View):

    def get(self, req):
        form = forms.UserRegisterForm()
        context = {
            'form': form
        }
        return render(req, 'shop/login.html', context)

    def post(self, req):
        form = forms.UserRegisterForm(req.POST)
        if (form.is_valid()):
            print(form.cleaned_data)
            return redirect('index')
        else:
            form = forms.UserRegisterForm(req.POST)
            return render(req, 'shop/login.html', {'form': form})
