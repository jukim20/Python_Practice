def test(num):
    num += 1
    print("함수안", num)
num = 20
test(num)
print("함수밖", num)

def test1(num):
    num += 1
    return num
num = 20
num = test1(num)  # ==> 21
#  num = 21
print("함수밖2", num)  # 21

def test2():
    global num  # 전역변수 num
    num += 1
num = 20
test2()
print("함수밖3", num)


