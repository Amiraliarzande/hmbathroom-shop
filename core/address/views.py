from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView
from address.models import Address
from address.forms import AddressForm


class AddressListView(LoginRequiredMixin, View):
    template_name = 'address/address.html'

    def get(self, request, *args, **kwargs):
        addresses = Address.objects.filter(user=request.user)
        form = AddressForm()
        return render(request, self.template_name, {
            'addresses': addresses,
            'form': form,
            'show_form': False
        })

    def post(self, request, *args, **kwargs):
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            return redirect('address:address_list')
        
        addresses = Address.objects.filter(user=request.user)
        return render(request, self.template_name, {
            'addresses': addresses,
            'form': form,
            'show_form': True
        })


class AddressUpdateView(LoginRequiredMixin, UpdateView):
    model = Address
    form_class = AddressForm
    template_name = 'address/address.html'
    success_url = reverse_lazy('address:address_list')

    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['addresses'] = Address.objects.filter(user=self.request.user)
        context['show_form'] = True
        return context