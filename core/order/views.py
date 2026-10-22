from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import View
from django.views.generic import ListView
from cart.models import Cart
from order.models import Order, OrderItem


class CreateOrderView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        try:
            cart = Cart.objects.get(user=request.user)
        except Cart.DoesNotExist:
            return redirect('cart:cart_detail')

        cart_items = cart.items.all()
        if not cart_items.exists():
            return redirect('cart:cart_detail')

        default_address = request.user.addresses.filter(is_default=True).first()
        if not default_address:
            default_address = request.user.addresses.first()

        order = Order.objects.create(
            user=request.user,
            address=default_address,
            total_price=cart.get_total_price,
            status='AWAITING'
        )

        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                price=item.product.price if item.product.price else 0,
                quantity=item.quantity
            )

        cart_items.delete()

        return redirect('order:order_list')


class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'order/orders.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)[:5]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_orders = Order.objects.filter(user=self.request.user)
        context['total_orders_count'] = user_orders.count()
        context['awaiting_count'] = user_orders.filter(status='AWAITING').count()
        context['dispatched_count'] = user_orders.filter(status='DISPATCHED').count()
        return context


class OrderHistoryView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'order/order-history.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)