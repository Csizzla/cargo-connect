
from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['departure_city', 'delivery_city', 'weight', 'dimensions',
                  'name', 'email', 'phone', 'message']


class DeliverySearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=True)


