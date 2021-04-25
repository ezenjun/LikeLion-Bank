from Bank import Menu

Continue = True
while Continue:
    print("======Bank Menu======")
    print("1. 계좌개설")
    print("2. 입금하기")
    print("3. 출금하기")
    print("4. 전체조회")
    print("5. 종료하기")
    print("=====================")
    select = int(input("선택할 숫자 입력: "))
    Continue = Menu.whichMenu(select)
