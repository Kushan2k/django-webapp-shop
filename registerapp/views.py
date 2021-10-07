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
        return render(req, 'user/register.html', context)

    def post(self, req):
        form = forms.UserRegisterForm(req.POST)
        if (form.is_valid()):
            print(form.cleaned_data)
            form.save()
            return redirect('login')
        return redirect('login')
