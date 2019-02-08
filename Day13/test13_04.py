#  배달 게임
end = False
des_x = 5
des_y = -8
x = 0
y = 0
speed = 1
max_speed = 3
dir = 0  # 0,1,2,3 으로 동서남북을 표현할수있다.
# 조건) 속도는  max_speed 를 넘을수없다  // 추가조건)은 목적지에 도달하면 새로운목적지 랜덤설정)
# 심화조건 ) 동서남북 구현
def show_menu():
    print("======== 배달게임 ==========")
    print("목적지 : ", des_x, ",", des_y)  # -10 ~ 10
    print("현재 위치 x :", x, ",y :", y, "속도 : ", speed, "방향", dir)
    print("1. 전진")
    print("2. 좌회전")
    print("3. 우회전")
    print("4. 후진")
    print("5. 속도조절")
    print("6. 배달")
    print("===================================")
def go_forward(dir, speed , x , y):
    if dir == 0:
        y += speed
    elif dir == 1:
        x += speed
    elif dir == 2:
        y -= speed
    elif dir == 3:
        x -= speed
    return x, y  # 2개 이상 반환될떄는 튜플(리스트)에 저장되어 반환된다 ==> 잘라서써야된다
while end == False:
    show_menu()
    sel = int(input("번호를 입력하세요 >>> "))
    if sel == 1:
        data = go_forward(dir, speed, x, y)
        x = data[0]
        y = data[1]
    if sel == 2:  # 0,1,2,3, (-1 은 예외처리)
        dir -= 1
        if dir < 0:
            dir = 3
    if sel == 3:
        dir += 1
        if dir > 3:
            dir = 0
    if sel == 5:
        selnum = int(input("속도(1~3)를 입력하세요 >>> "))
        speed = selnum
