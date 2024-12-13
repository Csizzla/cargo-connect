from django import forms
from deliveryapp.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'