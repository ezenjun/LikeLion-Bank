class Account:
    
    def __init__(self, account, name, balance) :      #계좌개설
        self.account = account
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount


    def withdraw(self, amount):
        if(amount > self.balance):   #출금금액이 계좌 잔고 보다 많을때
            print("---출금불가---")
        else:
            self.balance -= amount
            print("---출금완료---")
    
    def printinfo(self):
        print("AccountNum: %d, name: %s, balance: %d" %(self.account, self.name, self.balance))