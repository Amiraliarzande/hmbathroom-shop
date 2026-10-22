from django import forms


class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(
        min_value=1,
        max_value=99,
        initial=1,
        widget=forms.NumberInput(attrs={
            'class': 'qty-input',
            'min': '1',
            'max': '99',
            'aria-label': 'Quantity'
        })
    )
    update_quantity = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )