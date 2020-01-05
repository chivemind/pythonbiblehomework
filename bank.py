#Create Bank Account template
class Account:
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance
        
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print("Sorry, not enough funds.")
    
    def statement(self):
        print("Account Balance: ${}".format(self.balance))
 
#Create Active Current acount
class Current(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = -1000)
        
    def __str__(self):
        return "{}'s Current Amount: Balance ${}".format(self.name, self.balance)

#Create Savings Account
class Savings(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = 0)
        
    def __str__(self):
        return "{}'s Savings Amount: Balance ${}".format(self.name, self.balance)

#Test run data
R = Current("Ryan", 500)
print(R)
R.deposit(400)
print(R)
R.withdraw(2000)

T = Savings("Tom", 750)
print(T)
T.deposit(200)
print(T)
T.withdraw(1000)
