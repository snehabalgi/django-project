from django import forms
from .models import Coffee

class CoffeeForm(forms.ModelForm):
    class Meta:
        model = Coffee
        fields = ['name', 'price', 'quantity', 'image']

    # Add custom class to the 'name' field
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    # Remove description field as it is not in the model
    # If you want to add a description field, you would need to add it to the model first

    # Use FloatField for price to match the model
    price = forms.FloatField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    quantity = forms.IntegerField(
        min_value=1, 
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'type': 'file'})
    )
