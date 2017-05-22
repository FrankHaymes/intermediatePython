class ShippingContainer:
    next_serial = 1337

    def __init__(self, owner_code, contents):
        self._owner = owner_code
        self._contents = contents
        ShippingContainer.next_serial += 1
