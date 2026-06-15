from django import forms
from .models import Product  # предполагаем, что модель Product есть в models.py

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']