class AddToCartUseCase:
    def __init__(self, cart_repo):
       self.cart_repo = cart_repo


def execute(self, cart_id, book, quantity):
    cart = self.cart_repo.get(cart_id)
    cart.add_item(book, quantity)
    self.cart_repo.save(cart)