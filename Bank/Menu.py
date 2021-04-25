from .Account import Account                         

Account_List = []

def whichMenu(input):
    if input == 1:    #계좌개설
        OpenAccount()
        return True
    elif input == 2:  #입금하기
        deposit()
        return True
    elif input == 3:  #출금하기
        withdraw()
        return True
    elif input == 4:  #전체조회
        checkAll()
        return True
    elif input == 5:  #계좌이름변경
        change()
        return True 
    elif input == 6:  #종료하기
        print("안녕히가세요")
        return False
    else:             #잘못된 input
        print("1-5 사이의 숫자를 입력해주세요")
        return True

def OpenAccount():
    print("")
    print("======계좌 개설 메뉴======")
    while(True):
        try:
            accountNum = int(input("계좌번호: "))
            break
        except(ValueError):
            print("숫자를 입력하세요")
    
    while(True):
        name = input("이름: ")
        try:
            int(name)
            print("잘못된입력입니다")
        except:
            break
    while(True):
        try:
            initBalance = int(input("초기금액: "))
            break
        except(ValueError):
            print("숫자를 입력하세요")

    newAccount = Account(accountNum, name, initBalance)
    Account_List.append(newAccount)
    print("**계좌 개설을 완료했습니다. 감사합니다**")
    

def deposit():
    print("")
    print("======입금 메뉴======")
    while(True):
        try:
            accountNum = int(input("입금할 계좌번호: "))
            break
        except(ValueError):
            print("숫자를 입력하세요")
    #계좌번호에 해당하는 정보 출력
    depositAccount = findAccount(accountNum)
    if depositAccount == False: 
        print ("----없는 계좌 입니다.----")
        return
    while(True):
        try:
            depositAmount =  int(input("입금하실 금액: "))
            break
        except(ValueError):
            print("숫자를 입력하세요")
    #account 에 대해 Account.py의 deposit함수 실행
    depositAccount.deposit(depositAmount)
    #계좌번호에 해당하는 정보 출력
    depositAccount.printinfo()


def withdraw():
    print("")
    print("======출금 메뉴======")
    while(True):
        try:
            accountNum = int(input("출금하실 계좌번호: "))
            break
        except(ValueError):
            print("숫자를 입력하세요")
    #계좌번호에 해당하는 정보 출력
    withdrawAccount = findAccount(accountNum)
    if withdrawAccount == False: 
        print ("----없는 계좌 입니다.----")
        return
    while(True):
        try:
            withdrawAmount = int(input("출금하실 금액: "))
            break
        except(ValueError):
            print("숫자를 입력하세요")
    #account 에 대해 Account.py의 withdraw함수 실행
    withdrawAccount.withdraw(withdrawAmount)
    #계좌번호에 해당하는 정보 출력
    withdrawAccount.printinfo()

def checkAll():
    print("")
    print("======전체조회 메뉴======")
    for i in Account_List:
        i.printinfo()

def change():
    print("")
    print("======계좌이름변경======")
    while(True):
        try:
            accountNum = int(input("이름을 변경할 계좌번호: "))
            break
        except(ValueError):
            print("숫자를 입력하세요")
    changeAccount = findAccount(accountNum)
    if changeAccount == False: 
        print ("----없는 계좌 입니다.----")
        return  
    while(True):
        changename = input("변경할 이름: ")
        try:
            int(changename)
            print("잘못된입력입니다")
        except:
            break
    changeAccount.change(changename) 
    changeAccount.printinfo()



def findAccount(accountNum):
    for i in Account_List:
        if i.account == accountNum:
            i.printinfo()
            return i
    return False
