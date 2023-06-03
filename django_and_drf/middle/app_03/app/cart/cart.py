from decimal import Decimal
from django.conf import settings
from shop.models import Product

class Cart:

    def __init__(self, request: str) -> None:
        """Cart class initialisation""" 

        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            # empty
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product: str, quantity: int=1, override_quantity: bool=False) -> None:
        """Added product in cart or update quantity""" 

        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self) -> None:
        """Mark session for changed"""

        self.session.modified = True

    def remove(self, product: str) -> None:
        """Removed product from cart""" 

        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self) -> None:
        """Forloop for product in cart and getting from db""" 

        product_ids = self.cart.keys()
        # getting product and added in cart 
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        
        for product in products:
            cart[str(product.id)]['product'] = product
        
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self) -> int:
        """Len of product in cart"""

        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self) -> Decimal:
        """Full summ all products in cart""" 

        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
    

    def clear(self) -> None:
        """Delete car from session"""

        del self.session[settings.CART_SESSION_ID]
        self.save()