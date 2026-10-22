from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from account.models import Profile
from account.forms.profile import ProfileForm


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'account/profile.html'
    success_url = reverse_lazy('account:profile')

    def get_object(self, queryset=None):
        return self.request.user.profile