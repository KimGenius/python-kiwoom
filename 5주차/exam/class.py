class Account:
    accountNumber = ''
    balance = ''

    def __init__(self, accountNumber, balance):
        self.accountNumber = accountNumber
        self.balance = balance

    def charge(self, balance):
        self.balance += balance

    def printBalance(self):
        print(self.balance)


user1 = Account('1000-0000', 10000)
user1.printBalance()
user2 = Account('1000-0001', 10000)
user2.printBalance()
user3 = Account('1000-0002', 10000)
user3.printBalance()

user1.charge(30000)
user1.printBalance()
