class Customer:
    
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkeness = 0

    def deduct_from_wallet(self, amount):
        self.wallet -= amount

    def check_money(self, amount):
        return self.wallet >= amount
    
    def drink_drink(self, drink):
        self.drunkeness += drink.alcohol_level

    