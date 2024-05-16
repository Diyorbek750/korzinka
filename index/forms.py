from django import forms

class QuantityForm(forms.ModelForm):
    quantity1 = forms.IntegerField(label='Product 1 quantity', initial=0, min_value=0)