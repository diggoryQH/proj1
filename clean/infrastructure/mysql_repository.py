from interfaces.repositories import CartRepository
from domain.entities import Cart


class MySQLCartRepository(CartRepository):
    def get(self, cart_id):
        return Cart(cart_id)


    def save(self, cart):
        pass