from django.urls import path
from address.views import AddressListView, AddressUpdateView

app_name = 'address'

urlpatterns = [
    path('', AddressListView.as_view(), name='address_list'),
    path('<int:pk>/edit/', AddressUpdateView.as_view(), name='address_edit'),
]