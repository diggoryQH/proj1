class CartRepository:
    def get(self, cart_id):
        raise NotImplementedError

    def save(self, cart):
        raise NotImplementedError