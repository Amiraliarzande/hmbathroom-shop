from django import forms
from account.models import Profile


class ProfileForm(forms.ModelForm):
    
    email = forms.EmailField(
        disabled=True, 
        required=False,
        widget=forms.EmailInput(attrs={'autocomplete': 'email', 'placeholder': 'you@example.com'})
    )

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'phone', 'birth_date']
        widgets = {
            'first_name': forms.TextInput(attrs={'autocomplete': 'given-name', 'placeholder': 'Alex'}),
            'last_name': forms.TextInput(attrs={'autocomplete': 'family-name', 'placeholder': 'Morgan'}),
            'phone': forms.TextInput(attrs={'autocomplete': 'tel', 'placeholder': '07400 123456'}),
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.user:
            self.fields['email'].initial = self.instance.user.email