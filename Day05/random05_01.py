import random

ran = random.randint(0, 2)  # 0 ~ 2 사이의 랜덤값이 나온다.
print(ran)

coin = random.randint(0, 1)
select = int(input("앞(0) , 뒤(1) 를 입력하세요 >>> "))
if select == coin:
    print("정답")
# pass 는 조건만 잠시 쓸때 사용한다 식을쓸때는 지워야된다
# 1) 동전의 앞뒤를 맞추는게임
# 2) 홀짝을 맞추는 게임을 만들어보세요
coin = random.randint(1, 10)
# 3) 가위(0) 바위(1) 보(2) 게임을 만들어보자 (ai 는 랜덤으로 고른다)
