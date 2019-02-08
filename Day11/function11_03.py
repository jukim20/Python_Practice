"""
1. 입력 출력
2. 자료구조 ==> 1. 변수, 2. 리스트, 3. 함수, 클래스 (함수 여러개)
3. 알고리즘 ==> 1. 연산자, 2. if(조건문), 3. 반복문(while), 4. 이중반복문
# 리스트
"""

# 함수, 인자0, 인자1, 인자2


def show_num(num):
    print(num)


show_num(3)
num1 = 3
show_num(num1)


def calc(num1, num2):
    print(num1 - num2)


calc(10, 2)
num1 = 20
num2 = 30
calc(num1, num2)


lst = [0, 1, 2, 3, 4, 5]


def show_list(lst1):
    for i in lst1:
        print(i, end=" ")


show_list(lst)

# 문제 1) 리스트 안의 짝수만 출력해주는 함수
print()


def show_even_list(lst1):
    for i in lst1:
        if i % 2 == 0:
            print(i, end=" ")


show_even_list(lst)

# 문제 2) 리스트 안의 짝수의 갯수를 출력해주는 함수
print()


def show_num_even(lst1):
    num_even = 0
    for i in lst1:
        if i % 2 == 0:
            num_even += 1
    print("짝수의 갯수 : ", num_even)


show_num_even(lst)

# 문제 3) 리스트 안의 모든 합을 출력해주는 함수


def add_all_lst(lst1):
    total = 0
    for i in lst1:
        total += lst[i]
    print("총 합: ", total)


add_all_lst(lst)

# 응용문제 4) 리스트 2개를 인자로 사용해서 둘의 같은 인덱스끼리의 합을 출력해주는 함수
# 예) lst1 = [1, 2, 3], lst2 = [4, 5, 6], lst_result = [5, 7, 9]


def add_lists(lst1, lst2):
    lst_result = []
    for i in lst1 and lst2:
        lst_result.append(lst1[i] + lst2[i])
    print(lst_result)


add_lists([1, 2, 3], [4, 5, 6])
