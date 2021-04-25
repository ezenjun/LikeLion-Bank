class Account:
    log = []
    def __init__(self, account, name, balance) :      #계좌개설
        self.account = account
        self.name = name
        self.balance = balance
        strAccount = str(self.account)
        strName = str(self.name)
        strBalance = str(self.balance)
        message = "계좌 생성 - 계좌번호: " +str(self.account) + " 이름: "  +str(self.name) + " 초기예금: " +str(self.balance) + "원"
        self.log.append(message)

    def deposit(self, amount):
        self.balance += amount
        message = "입금 - " + str(amount) + "원"
        self.log.append(message)


    def withdraw(self, amount):
        if(amount > self.balance):   #출금금액이 계좌 잔고 보다 많을때
            print("---출금불가---")
            message = "출금 실패 - 잔액부족"
            self.log.append(message)
        else:
            self.balance -= amount
            print("---출금완료---")
            message = "출금 성공 - " + str(amount) + "원"
            self.log.append(message)
            return True

    def printinfo(self):
        print("AccountNum: %d, name: %s, balance: %d" %(self.account, self.name, self.balance))

    def printLog(self):
        print(self.log)