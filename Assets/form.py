from django import forms
from .models import Product

class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'product_id': 'Product ID',
            'name': 'Name',
            'sku': 'SKU',
            'quantity': 'Quantity',
            'price': 'Price',
            'supplier': 'Supplier',

        }

        widgets = {
            'product_id': forms.NumberInput(attrs={'placeholder': 'e.g. 1', 'class':'form-control'}),
            'name': forms.TextInput(attrs={'placeholder': 'e.g. Black Shoes', 'class':'form-control'}),
            'sku': forms.TextInput(attrs={'placeholder': 'e.g. S12345', 'class':'form-control'}),
            'quantity': forms.NumberInput(attrs={'placeholder': 'e.g. 1', 'class':'form-control'}),
            'price': forms.NumberInput(attrs={'placeholder': 'e.g. 4.99', 'class':'form-control'}),
            'supplier': forms.TextInput(attrs={'placeholder': 'e.g. XYZ Corp', 'class':'form-control'}),
        }