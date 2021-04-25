from Bank import Menu

Continue = True
while Continue:
    print("======Bank Menu======")
    print("1. 계좌개설")
    print("2. 입금하기")
    print("3. 출금하기")
    print("4. 전체조회")
    print("5. 계좌이름변경")
    print("6. 종료하기")
    print("=====================")
    while(True):
        try:
            select = int(input("선택할 숫자 입력: "))
            break
        except(ValueError):
            print("숫자를 입력하세요")
    
    Continue = Menu.whichMenu(select)
