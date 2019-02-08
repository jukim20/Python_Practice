import random

# 문제 1) 동전게임을 반복해서 실행한다
#           조건 1) 돈이 다 떨어지면 종료 (1판에 300원)
#           조건 2 ) 1승에 500원씩 추가
money = 1000
coin = random.randint(0, 1)
game_over = False

while game_over == False:
    # if True:
    # game_over: True
    guess = int(input("앞면 (0) 과 뒷면 (1) 중 하나를 고르세요."))
    print(coin)
    money -= 300

    if coin == guess:
        print("맞췄습니다!")
        money += 500
        print("남은 돈은", money, "원입니다.")
    else:
        print("틀렸습니다! 다시 도전하세요.")
        print("남은 돈은", money, "원입니다.")

    if money < 300:
        game_over = True
        print("게임이 종료되었습니다.")

