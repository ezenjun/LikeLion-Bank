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
    elif input == 5:  #종료하기
        return False
    else:             #잘못된 input
        print("잘못된입력입니다")
        return True

def OpenAccount():
    print("계좌 개설 메뉴 입니다.")
    accountNum = int(input("계좌번호: "))
    name = input("이름: ")
    initBalance = int(input("초기금액: "))
    newAccount = Account(accountNum, name, initBalance)
    Account_List.append(newAccount)
    print("**계좌 개설을 완료했습니다. 감사합니다**")
    

def deposit():
    print("입금 메뉴 입니다.")
    accountNum = input("입금할 계좌번호: ")
    #계좌번호에 해당하는 정보 출력
    depositAccount = findAccount()
    depositAmount = input("입금하실 금액: ")
    #account 에 대해 Account.py의 deposit함수 실행
    print(type(depositAccount))
    depositAccount.deposit(depositAmount)
    #계좌번호에 해당하는 정보 출력
    depositAccount.printinfo()
    print("**입금을 완료했습니다.**")


def withdraw():
    print("출금 메뉴 입니다.")
    accountNum = input("출금하실 계좌번호: ")
    #계좌번호에 해당하는 정보 출력
    withdrawAccount = findAccount()
    withdrawAmount = input("출금하실 금액: ")
    #account 에 대해 Account.py의 withdraw함수 실행
    withdrawAccount.withdraw(withdrawAmount)
    #계좌번호에 해당하는 정보 출력
    withdrawAccount.printinfo()
    print("**출금을 완료했습니다.**")

def checkAll():
    print("전체조회 메뉴 입니다.")
    for i in Account_List:
        print(i.printinfo())

def findAccount():
    for i in Account_List:
        if i.account == accountNum:
            i.printinfo()
            return i
        return 0
