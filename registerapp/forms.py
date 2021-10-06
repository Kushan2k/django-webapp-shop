from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    number = forms.CharField(max_length=12)
    city = forms.CharField(max_length=50)

    class Meta:
        model = User

        fields = ['username', 'email', 'number',
                  'city', 'password1', 'password2']
