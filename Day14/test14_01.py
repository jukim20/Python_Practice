#  변수의 생명주기 : 지역변수 , 전역변수
#       1) 전역변수 : 프로그램이 시작해서 종료될때 메모리에서 해제
#       2) 지역변수 : 함수안에서 생성되서 함수가 종료될때 해제
def test():
    num = 10
num = 20
test()
while True:
    sel = input("quit 을 입력하세요 ")
    if sel == "quit":
        break
test()
test()
print(num)
def test2(num):
    num * num
    return num
num = test2()
print(num)
def test3():
    num = 10
test3()
def test4(num):
    num = 20
test4(10)