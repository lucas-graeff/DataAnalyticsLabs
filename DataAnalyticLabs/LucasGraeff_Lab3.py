import random
from unicodedata import name

class CreditCard:

    def __init__(self, cardNumber, name, expiration):
        self.cardNumber = cardNumber
        self.name = name
        self.expiration = expiration
        self.creditLimit = 1000
        self.balance = random.randrange(0,1000)
        self.cardType = {
            1: "Visa",
            2: "Master",
            3: "Amex",
            4: "Discover"
        }
        self.set_cardType()

    def get_cardOwner(self):
        return self.name

    def set_cardOwner(self, x):
        self.name = x
    
    def get_cardType(self):
        return self.cardType
    
    def set_cardType(self):
        fifthNum = int(self.cardNumber[5])
        if fifthNum > 0 and fifthNum < 5:
            self.cardType = self.cardType[fifthNum]
        else:
            self.cardType = 'Not Supported Card Type'

    def processOrder(self, price):
        if self.get_cardType() != 'Not Supported Card Type':
         if price < self.balance:
             self.balance - price
             return True
        else:
            return False
    
    def __str__(self):
        return f'{self.name} is the owner of the credit card with number {self.cardNumber} which expires on {self.expiration}'


