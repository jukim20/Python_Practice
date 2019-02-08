"""
1. print (출력)
2. 변수 (variable)
3. input (입력)
4. 연산  ==> 1. (=)  2. ( + - * / % )  3. ( == > < != >= <=)
5. casting ==> 형변환 (input 해결)
6. 조건문 ==> if 문
"""

# 문제 1) 숫자를 입력받고 5의 배수이면서 3의 배수인지 체크해보세요

num = int(input("숫자를 입력하세요 >>> "))

if num % 5 == 0:
    if num % 3 == 0:
        print("True")
    else:
        print("False")
else:
    print("False")
