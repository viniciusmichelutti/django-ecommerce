from shop.models import Product


class ProductGateway:
    def get_available_products(self):
        return Product.objects.filter(available=True)
