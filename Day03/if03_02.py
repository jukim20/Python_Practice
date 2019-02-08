# 산술연산자 ==> (+) (-) (*) (/) (%)
# 대입연산자 ==> (=)

# 비교연산자
"""
    1. a == b   :   a 와 b 가 같으면 True
    2. a != b   :   a 와 b 가 다르면 True
    3. a > b    :   a 가 b 보다 크면 True
    4. a < b    :   a 가 b 보다 작으면 True
    5. a >= b   :   a 가 b 보다 크거나 같으면 True
    6. a <= b   :   a 가 b 보다 작거나 같으면 True
"""

print(10 == 10)  # True
print(10 != 10)  # False

a = 10
b = 10
print(a == b)

a = 10
b = 20
print(a != b)

a = 20
b = 10
print(a > b)

b = 30
print(a < b)

a = 30
print(a >= b)

b = 40
print(a <= b)
