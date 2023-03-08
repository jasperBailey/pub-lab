class Customer:
    
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def deduct_from_wallet(self, amount):
        self.wallet -= amount

    def buy_drink(self, pub, drink_name):
        drink = pub.find_drink_by_name(drink_name)
        if drink != None:
            if self.wallet < drink.price:
                print("GET OUT OF MY PUB!")
            else:
                self.deduct_from_wallet(drink.price)
                pub.add_money_to_till(drink.price)

    