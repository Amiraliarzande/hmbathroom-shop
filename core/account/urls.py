from django.urls import path
from account.views import SignInView, SignUpView, ProfileUpdateView

app_name = 'account'

urlpatterns = [
    path('login/', SignInView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', ProfileUpdateView.as_view(), name='profile'),
]