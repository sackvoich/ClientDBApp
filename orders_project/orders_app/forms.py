from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'order_amount': forms.NumberInput(attrs={'step': '0.01'}),
        }