import random

# 임시 변수 만들어놓을 때 사용

x = int()  # int 정수 ==> 빈 정수 변수를 하나 만든다
y = int()
z = None  # 보통 None 이나 0 을 쓴다
k = 0
s = ""
r = str()

# 배달 게임
end = False
des_x = random.randint(-10, 10)
des_y = random.randint(-10, 10)
x = 0
y = 0
speed = 1
max_speed = 3

# 조건 : 속도는 max_speed 를 넘을 수 없다
# 추가조건: 목적지에 도달하면 새로운 목적지 랜덤 설정

while end == False:
    print("========== 배달게임 ==========")
    print("목적지 : ", des_x, ",", des_y)
    print("현재 위치 >> x : ", x, ", y : ", y, ", 속도 : ", speed)
    print("1. 전진")
    print("2. 좌회전")
    print("3. 우회전")
    print("4. 후진")
    print("5. 속도조절")
    print("6. 배달")

    print("=============================")

    select = int(input("선택지를 고르세요 >>> "))
    if select == 1:
        y += speed
    elif select == 2:
        x -= speed
    elif select == 3:
        x += speed
    elif select == 4:
        y -= speed
    elif select == 5:
        change_speed = int(input("속도를 (1~3) 조정하세요 >>> "))
        if change_speed <= 0 or change_speed > 3:
            print("속도는 1~3 사이어야 합니다.")
        if change_speed == 1:
            speed = 1
        if change_speed == 2:
            speed = 2
        else:
            speed = 3
    elif select == 6:
        if des_x == x and des_y == y:
            print("성공적으로 배달을 완료하였습니다! \n"
                  "게임을 다시 시작하시겠습니까?")
            restart = int(input("Yes (0) or No (1) >>> "))

            if restart == 0:
                des_x = random.randint(-10, 10)
                des_y = random.randint(-10, 10)
            elif restart == 1:
                print("게임이 종료됩니다. 플레이해주셔서 감사합니다.")
                end = True

            else:
                restart = int(input("올바른 선택지를 입력하세요 (0, 1) >>> "))

                if restart == 0:
                    des_x = random.randint(-10, 10)
                    des_y = random.randint(-10, 10)
                elif restart == 1:
                    end = True

        else:
            print("목적지가 아닙니다. 다시 시도하세요.")
    else:
        print("올바른 선택지를 입력하세요.")





