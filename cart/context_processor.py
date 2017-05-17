from cart.cart_session import CartSession


def cart(request):
    return { 'cart': CartSession(request) }