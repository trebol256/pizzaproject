from django import forms
from .models import Orderrequest

class OrderForm(forms.ModelForm):

    class Meta:
        model = Orderrequest
        fields = ['pizzatype', 'commentorder']