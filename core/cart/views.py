from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from shop.models import Product
from cart.models import Cart, CartItem
from cart.forms import AddToCartForm



def _get_or_create_cart(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key
        cart, created = Cart.objects.get_or_create(session_key=session_key, user=None)
    return cart


class CartDetailView(View):
    template_name = 'cart/cart.html'

    def get(self, request, *args, **kwargs):
        cart = _get_or_create_cart(request)
        return render(request, self.template_name, {'cart': cart})


class AddToCartView(View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id, is_active=True)
        cart = _get_or_create_cart(request)
        
        form = AddToCartForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            quantity = cd['quantity']
            update_quantity = cd['update_quantity']
            
            cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
            if update_quantity:
                cart_item.quantity = quantity
            else:
                cart_item.quantity += quantity
            cart_item.save()
            
        return redirect('cart:cart_detail')


class UpdateCartItemView(View):
    def post(self, request, item_id):
        cart_item = get_object_or_404(CartItem, id=item_id)
        quantity = int(request.POST.get('quantity', 1))
        
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()
            
        return redirect('cart:cart_detail')


class RemoveFromCartView(View):
    def get(self, request, item_id):
        cart_item = get_object_or_404(CartItem, id=item_id)
        cart_item.delete()
        return redirect('cart:cart_detail')