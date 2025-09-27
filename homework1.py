class Bank_account:
    def __init__(self,account_number,balance):
        self.account_number  = account_number 
        self.balance = balance
    def deposit(self,amount):
        self.balance  += amount
        return self.balance 
    def withdraw(self,amount):
       
        if amount > self.balance:
            print("Сума завелика!")
        else:
            self.balance -= amount
        return self.balance
    
User_1 = Bank_account(1,500)
User_2 = Bank_account(2,100)

print(User_1.deposit(750))
print(User_1.withdraw(1900))

print(User_2.withdraw(257))
print(User_1.deposit(3783))


