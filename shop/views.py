from django.shortcuts import render, get_object_or_404

from cart.forms import CartAddProductForm
from shop.gateways.product_gateway import ProductGateway
from shop.models import Category, Product


def product_list(request, category_slug=None):
    product_gateway = ProductGateway()
    category = None
    categories = Category.objects.all()
    products = product_gateway.get_available_products()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request, 'shop/product/list.html', {
        'categories': categories,
        'category': category,
        'products': products
    })

def product_detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug, available=True)
    cart_add_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {
        'product': product,
        'cart_add_form': cart_add_form
    })
