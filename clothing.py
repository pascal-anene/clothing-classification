from itertools import count


class Clothing:

    def __init__(self, color, size, style, price) -> None:
        self.color = color
        self.size = size
        self.style = style
        self.price = price

    def change_price(self, price):
        self.price = price

    def calculate_discount(self, discount):
        return self.price * (1 - discount)

    def calculate_shipping(self, weight, rate):
        return weight * rate

# The Following Classes Inherit from the Clothing Class

class Shirt(Clothing):

    def __init__(self, color, size, style, price, long_or_short) -> None:
        Clothing.__init__(self, color, size, style, price)
        self.long_or_short = long_or_short

    def double_price(self):
        self.price = 2*self.price

class Pants(Clothing):

    def __init__(self, color, size, style, price, waist) -> None:
        Clothing.__init__(self, color, size, style, price)
        self.waist = waist

    def calculate_discount(self, discount):
        return self.price * (1 - discount / 2)

class Blouse(Clothing):

    def __init__(self, color, size, style, price, country_of_origin) -> None:
        Clothing.__init__(self, color, size, style, price)
        self.country_of_origin = country_of_origin

    def triple_price(self):
        return 3 * self.price
        

