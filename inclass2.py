class ShoppingCart:
    """A shopping cart"""

    def __init__(self,items,coupons):
        
        self.items = list(items)
        self.coupons = list(coupons)

    def coupon(self,coupons):
        for item in items:
            final_price = item - coupons

my_cart = ShoppingCart