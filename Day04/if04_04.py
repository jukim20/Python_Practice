print("***코리아 홍콩반점***")
print("1. 짜장면  :   6000원")
print("2. 짬뽕    :   7000원")
print("3. 탕수육  :   12000원")

select = int(input("번호를 입력하세요 >>> "))
money = int(input("내실 돈의 액수를 적어주세요. >>> "))

# 문제 1) 이상한 번호 입력시 경고 메세지
# 문제 2) 음식메뉴 출력 거스름돈 출력

if select == 1:
    if money >= 6000:
        print("거스름돈은 ", money - 6000, "원입니다.")
    else:
        print("돈이 ", 6000 - money, "원 부족합니다.")

elif select == 2:
    if money >= 7000:
        print("거스름돈은", money - 7000, "원입니다.")
    else:
        print("돈이", 7000 - money, "원 부족합니다.")
elif select == 3:
    if money >= 12000:
        print("거스름돈은", money - 12000, "원입니다.")
    else:
        print("돈이", 12000 - money, "원 부족합니다.")
else:
    print("1~3번 사이의 메뉴를 골라주세요.")

