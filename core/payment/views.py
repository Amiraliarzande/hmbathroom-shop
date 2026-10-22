from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class PaymentView(LoginRequiredMixin, TemplateView):
    template_name = 'payment/payment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        default_address = user.addresses.filter(is_default=True).first()
        if not default_address:
            default_address = user.addresses.first()
        
        context['default_address'] = default_address
        return context