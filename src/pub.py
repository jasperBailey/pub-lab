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
            
    def request_serve_drink(self, customer, drink_name):
        # check customer_age
        # check find_drink_by_name
        # check customer has enough money
        # if all True, call serve drink function

        drink = self.find_drink_by_name(drink_name)
        if drink != None:
            if customer.check_money(drink.price) and \
            customer.age >= 18 and customer.drunkeness <= 15:
                customer.deduct_from_wallet(drink.price)
                self.add_money_to_till(drink.price)
                customer.drink_drink(drink)
            else:
                print("GET OUT OF MY PUB!")

    