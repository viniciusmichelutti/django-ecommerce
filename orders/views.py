from django.shortcuts import render

from cart.cart_session import CartSession
from orders.forms import OrderCreateForm
from orders.models import OrderItem
from orders.tasks import order_created


def create_order(request):
    cart = CartSession(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])

            cart.clear()
            order_created.delay(order.id)
            return render(request, 'orders/order/created.html', { 'order': order })
    else:
        form = OrderCreateForm()

    return render(request, 'orders/order/create.html', { 'cart': cart, 'form': form })
