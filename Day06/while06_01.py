# 앞뒤맞추는 동전게임

# 반복문 ==> while 문
"""
1. while ==> 키워드
2. 조건: ==> 조건종료 ==> 조건이 True면 실행문 실행
3. 들여쓰기 ==> 들여쓰기 해서 작성한 명령문을 실행한다. 단 종료후 다시 조건으로 올라간다.
4. 반드시 탈출조건이 필요하다.
        1) 초기식 (tree_hit = 0)
        2) 조건식 (tree_hit < 10:)
        3) 증감식 (tree_hit += 1)
"""
if True:
    print("이프문")  # 이프문은 조건이 True 면 실행문이 실행되고 종료

# while True:
#    print("반복문")  # 반복문은 조건이 True 면 실행문이 실행되고 다시 조건으로 올라간다.

tree_hit = 0
while tree_hit < 10:
    print("나무를 찍는다.")
    tree_hit += 1
print("나무가 넘어간다!")

# 문제 1) 0~9 까지 숫자를 출력해보자

num = 0
while num < 10:
    print(num)
    num += 1

# 문제 2) 10~20까지 숫자를 출력해보자

while num <= 20:
    print(num)
    num += 1
