print("***코리아홍콩반점***")
print("1. 짜장면  :  6000원")
print("2. 짬뽕    :  7000원")
print("3. 탕수육  : 12000원")
select = int(input("번호를 입력하세요 >>> "))
money = 10000
jja = 6000
bbong = 7000
tang = 12000
if select <= 0 or select > 3:
    print("번호를 잘못입력했습니다")
if select == 1:
    if money > jja:
        money = money - jja
        print("거스름돈 >>> ", money)
    else:
        print("돈이 부족합니다")
# 문제 2) 음식메뉴 출력 거스름돈 출력
# 문제 1) 이상한번호 입력시 경고메세지
# 문제 )성적을 하나 입력받고 100~91 ==> A , 90~ 81 ==> B , 이하 재시험 (논리연산자 사용)


