from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm

User = get_user_model()


class SignUpForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'At least 8 characters', 'minlength': '8'}),
        label='Password'
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}),
        label='Confirm Password'
    )

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'you@example.com'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Alex'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Morgan'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('An account with this email already exists.')
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', 'Passwords do not match.')
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            profile = user.profile
            profile.first_name = self.cleaned_data.get('first_name', '')
            profile.last_name = self.cleaned_data.get('last_name', '')
            profile.save()
        return user


class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        label='Email address',
        widget=forms.EmailInput(attrs={'autocomplete': 'email', 'placeholder': 'you@example.com'})
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'placeholder': 'At least 8 characters'})
    )