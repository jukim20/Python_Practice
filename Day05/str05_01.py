# string 문자열(여러글자)
# 변수는 값을 한가지밖에 저장할수 없다.
str1 = "안녕하세요"
print(str1)
num = 10
# 1. 여러줄 표현하기
print("1. no pain"
      "no gain")
# 2. 쌍따옴표 3개
print("""
2. no pain
no gain""")
print('''
3. no pain
no gain
''')
# 이스케이프문자 활용:
# escape 문자
"""
\n          : 문자열 안에서 줄을바꾸고 싶을때 사용(new line)
\t          : 문자열 사이에서 간격을 줄때 사용(tab)
\\          : 문자 \ 를 표현하고 싶을때 사용
\'          : 홑따옴표를 표현할때 사용
\"          : 쌍따옴표를 표현할때 사용
"""
print("안녕\n하세요")
print("역슬래쉬\\")  # 역슬래쉬\
print("쌍따옴표\"")  # 쌍따옴표"
print("탭\t탭")



