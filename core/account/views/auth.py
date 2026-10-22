from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from account.forms.user import SignUpForm, LoginForm


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'account/signup.html'
    success_url = reverse_lazy('account:login')

    def form_valid(self, form):
        response = super().form_valid(form)
        return response


class SignInView(LoginView):
    form_class = LoginForm
    template_name = 'account/login.html'
    redirect_authenticated_user = True
    next_page = reverse_lazy('home')