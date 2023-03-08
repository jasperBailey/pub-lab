class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self._drinks = []

    def add_drink(self, drink):
        self._drinks.append(drink)

    def get_drinks(self):
        return self._drinks

    def add_money_to_till(self, amount):
        self.till += amount

    def find_drink_by_name(self, drink_name):
        for drink in self._drinks:
            if drink.name == drink_name:
                return drink

    