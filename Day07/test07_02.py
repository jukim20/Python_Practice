import random

# ============= 업다운 게임 ===============
num = random.randint(0, 100)
game_over = False
count = 0

while game_over == False:
    select = int(input("숫자를 맞춰보세요. >>> "))
    if select < 0 or select > 100:
        print("잘못 입력했습니다. 다시 입력하세요.")
    elif select > num:
        count += 1
        print("DOWN")
    elif select < num:
        count += 1
        print("UP")
    else:
        count += 1
        print("정답입니다! ", count, "번만에 맞췄습니다.")
        game_over = True

print("==============================================")
# ============= 가위바위보 ================

ai = random.randint(0,2)
select = int(input("가위 (0), 바위 (1), 보 (2) 중 하나를 내세요 >>> "))

if select == 0:
    if ai == 0:
        print("비겼습니다. 상대도 가위를 냈습니다.")
    elif ai == 1:
        print("졌습니다. 상대는 바위를 냈습니다.")
    else:
        print("이겼습니다! 상대는 보를 냈습니다.")
elif select == 1:
    if ai == 0:
        print("이겼습니다! 상대는 가위를 냈습니다.")
    elif ai == 1:
        print("비겼습니다. 상대도 바위를 냈습니다.")
    else:
        print("졌습니다. 상대는 보를 냈습니다.")
elif select == 2:
    if ai == 0:
        print("졌습니다. 상대는 가위를 냈습니다.")
    elif ai == 1:
        print("이겼습니다! 상대는 바위를 냈습니다.")
    else:
        print("비겼습니다. 상대도 보를 냈습니다")
else:
    print("잘못 입력했습니다.")

print("==============================================")
# =============== ATM ==================== 조건 1) 비밀번호, 조건 2) - 금액 안 나오도록 예외처리

end = False
money = 5000
pw = "1234"

print("================== ATM =======================")
print("1. 입금")
print("2. 출금")
print("3. 조회")
print("4. 종료")
print("==============================================")

enter_pw = input("비밀번호를 입력하세요.")
if enter_pw == pw:
    while end == False:
        select = int(input("원하시는 거래를 선택하세요 >>> "))
        if select == 1:
            insert = int(input("입금하실 금액을 입력하세요 >>> "))
            if insert > 0:
                money += insert
                print(insert, "원이 입금되었습니다. 현재 잔고는 ", money, "원 입니다.")
            else:
                print("올바른 금액을 입력해주세요.")
        elif select == 2:
            withdraw = int(input("출금하실 금액을 입력하세요 >>> "))
            if withdraw <= money:
                money -= withdraw
                print(withdraw, "원이 출금되었습니다. 현재 잔고는", money, "원 입니다.")
            else:
                print("잔고가 부족합니다.")
        elif select == 3:
            print("현재 잔고는 ", money, "원 입니다.")
        elif select == 4:
            print("시스템이 종료됩니다. 거래해주셔서 감사합니다.")
            end = True
        else:
            print("원하시는 거래를 다시 입력해주세요.")
else:
    print("비밀번호를 잘못 입력했습니다.")


print("==============================================")

# 기본문제 )
# 숫자 2개를 입력받고 ?? 가 ? 보다 크다 작다 같다 출력
num1 = int(input("숫자 1을 입력하세요 >>> "))
num2 = int(input("숫자 2를 입력하세요 >>> "))

if num1 > num2:
    print("숫자 1은 숫자 2보다 크다.")
elif num1 < num2:
    print("숫자 1은 숫자 2보다 작다.")
else:
    print("숫자 1은 숫자 2와 같다.")

print("==============================================")

# 숫자 1개를 입력받고 짝수 홀수 출력
num = int(input("숫자를 입력하세요 >>> "))
if num % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")

print("==============================================")

# 0 ~ 20까지 중 짝수만 출력
num = 0
while num <= 20:
    if num % 2 == 0:
        print(num)
    num += 1

print("==============================================")

# 0 ~ 10까지 다 더한 값 출력
num = 0
sum = 0
while num <= 10:
    sum += num
    num += 1
print(sum)
print("==============================================")