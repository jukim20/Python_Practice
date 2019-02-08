# 문제) 자기소개 를 변수를 사용해서 출력 (이름,나이,이메일,주소...)
name = "박병욱"
age = 20

# 응용문제 1) 10 , 3 을 변수에 저장후 10 + 3 = 13 (서식문자사용) 출력
num1 = 10
num2 = 3
print("%d + %d = %d" % (num1, num2, num1+num2))

# 1. print() ==> 출력
# 2. var ==> 저장
# 3. input() ==> 입력 후 저장 ==> 문자로 저장된다.
# 4. operator ==> 연산 ==> 계산  + - * / %
#       1) (숫자 + 숫자) => + - * / %
#       2) (문자 + 문자) => 뒤에 붙여넣기
# 5. casting ==> 형변환 ==> 자료형을 변화시킨다 "문자" ==> "숫자" , "숫자" ==> "문자"

print("쓰고싶은말")
email = "momk@naver.com"
print(email)
# address = input("주소를 입력하세요 >>> ")  # 엔터를 기다리고있다(소괄호안에 메세지입력가능)
# print(address)

print(10 + 10)  # 20
print("10" + "20")  # 1020

# 숫자 2개를 입력받고 더하기를 출력하세요
num1 = input("숫자 1 입력하세요 >>>")  # 10
num2 = input("숫자 2 입력하세요 >>>")  # 20

print(num1+num2)  # 1020 ; 문자니까 뒤에 붙여넣어짐

int(num1)  # 10
int(num2)  # 20
print(int(num1) + int(num2))  # casting; int 를 씌워준다
