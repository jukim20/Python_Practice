money = 100000
print("***코리아홍콩반점***")
print("1. 짜장면  :  6000원")
print("2. 짬뽕    :  7000원")
print("3. 탕수육  : 12000원")
print("4. 종료")
print("돈 : ", money)

jja = 6000
bbong = 7000
tang = 12000
jja_count = 1
end = False

# 조건1 ==> 반복문으로 변경
# 조건2 ==> 짜장면은 3그릇밖에 구입할수없다.(양념이다떨어짐)

while not end:
    select = int(input("번호를 입력하세요 >>> "))

    if select == 1:
        if jja_count > 3:
            print("양념이 다 떨어져 더 이상 짜장면을 주문할 수 없습니다.")
        else:
            if money > jja:
                jja_count += 1
                money -= jja
                print("거스름돈 : ", money)
            else:
                print("돈이 부족합니다.")
    elif select == 2:
        if money > bbong:
            money -= bbong
            print("거스름돈 : ", money)
        else:
            print("돈이 부족합니다.")
    elif select == 3:
        if money > tang:
            money -= tang
            print("거스름돈 : ", money)
        else:
            print("돈이 부족합니다.")
    elif select == 4:
        print("이용해주셔서 감사합니다.")
        end = True
    else:
        print("잘못 입력했습니다.")

print("==========================================")

# 기본문제 ==> 1) 숫자하나를 입력받고 짝수홀수 출력

num = int(input("숫자를 입력하세요 >>> "))
if num % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")

print("==========================================")

# 2) ==> 0~20까지 홀수만 출력
num = 0
while num <= 20:
    if num % 2 == 1:
        print(num)
    num += 1

print("==========================================")

# 3) ==> 0~20까지 짝수만 다 더한값 출력
num = 0
sum = 0
while num <= 20:
    if num % 2 == 0:
        sum += num
    num += 1
print(sum)

# 4) ==> 양수 한개 를 입력받고 0 ~ 양수까지의 모든합 출력

pos = int(input("양수를 하나 입력하세요 >>> "))
count = 0
sum = 0

if pos <= 0:
    print("잘못 입력했습니다.")
else:
    while count <= pos:
        sum += count
        count += 1

print(sum)
