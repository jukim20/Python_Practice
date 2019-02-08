# print() 출력
# input() 입력 ==> enter 를 누를 때까지 입력을 기다린다.

# input()  # Process finished with exit code 0

# 1. 숫자 ==> 연산시 우리가 알고 있는 연산을 해준다
# 2. 문자 ==> 연산시 뒤에 이어붙인다 (+)

num = input()  # 콘솔에 num 에 들어갈 정보를 넣고 enter 를 누르면 input 으로 들어온 정보가 num 에 저장된다
print(num)  # 10
print(num + num)  # 1010. 20 이 아님.

print(10 + 10)  # 20
print("10" + "10")  #1010

# 입력을 받으면 문자로 저장된다! 숫자도 숫자로 들어오지 않고 문자로 저장됨.

# 문제 1) 숫자 2개를 입력받고 산술연산을 출력하세요

# "ㅁㅇㄴㅁㄴㅇㅁㄴㅇ"
# "10" ==> 10 : 문자열로 저장이 되었어도 그 내용이 숫자면 숫자로 바꿔주는 방법이 있다.
# 이것을 casting (형변환) 이라고 한다.