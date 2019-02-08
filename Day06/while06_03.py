import random

# 업다운 게임
# 조건 1) ai 가 랜덤으로 0~100을 저장한다
# 조건 2) me 는 0~100을 직접 입력한다
# 조건 3) ai 와 me 를 비교후 크다 작다 같다 출력
# 조건 4) 위의 정보를 토대로 맞출 때까지 반복 (반복횟수 count 출력)

num = random.randint(0, 100)
game_over = False
count = 0

while game_over == False:
    guess = int(input("0~100 사이의 숫자를 맞춰보세요 >>> "))

    if guess < 0 or guess > 100:
        print("잘못 입력했습니다. 다시 입력하세요.")
    else:
        if guess > num:
            count += 1
            print("DOWN")
        elif guess < num:
            count += 1
            print("UP")
        else:
            count += 1
            print("맞췄습니다!", count, "번이 걸렸습니다.")
            game_over = True


