from django import forms
from address.models import Address


class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = [
            'label', 
            'full_name', 
            'address_line_1', 
            'address_line_2', 
            'city', 
            'postcode', 
            'country', 
            'phone', 
            'is_default'
        ]
        widgets = {
            'label': forms.TextInput(attrs={'placeholder': 'Home, Work…'}),
            'full_name': forms.TextInput(attrs={'autocomplete': 'name'}),
            'address_line_1': forms.TextInput(attrs={'autocomplete': 'address-line1'}),
            'address_line_2': forms.TextInput(attrs={'autocomplete': 'address-line2'}),
            'city': forms.TextInput(attrs={'autocomplete': 'address-level2'}),
            'postcode': forms.TextInput(attrs={'autocomplete': 'postal-code'}),
            'country': forms.Select(attrs={'autocomplete': 'country-name'}, choices=[
                ('United Kingdom', 'United Kingdom'),
                ('Ireland', 'Ireland'),
            ]),
            'phone': forms.TextInput(attrs={'autocomplete': 'tel'}),
        }