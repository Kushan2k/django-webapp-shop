from django import forms
from django.forms import ModelForm
from shop.models import Item,Images



class AddItemForm(ModelForm):
    

    class Meta:
        model=Item
        fields=['name','price']



class AddImageForm(ModelForm):
    

    class Meta:
        model=Images
        fields=['url']
        widgets={
            'files':forms.FileInput(attrs={'id':'files','multiple':True})
        }


    