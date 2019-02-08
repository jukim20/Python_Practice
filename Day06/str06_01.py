# 문자열 관련 함수
# 1. 길이 (len)  ***
str = "hahahahaha"
length = str.__len__()  # 언더바 2개씩 총 4개
print(length)

length = len(str)
print(length)

# 2. 개수 (count)
print("a의 개수 >>> ", str.count("a"))

# 3. 인덱스 위치 (index)
str = "Korea0It"
print("K 의 위치 >>> ", str.index("K"))

# 3-1 인덱스 위치 (find)
print("o 의 위치 >>> ", str.find("o"))  # 처음 찾은 글자만 반환한다. (중복글자 찾을 수 없음)

# 4. 소문자를 대문자로 바꾸기 (upper)
print(str.upper())  # KOREAIT

# 5. 대문자를 소문자로 바꾸기 (lower)
print(str.lower())  # koreait

# 문제 1) 소문자를 입력하든 대문자를 입력하든 섞어서 입력하든 단어만 맞으면 탈출시켜보자

db_pw = "quit"
pw = input("탈출명령어를 입력하세요 >>> ")
if pw.lower() == db_pw:
    print("탈출")
else:
    print("실패")

# 6. 문자열 바꾸기
str = "appleTree"
str = str.replace("apple", "lemon")
print(str)  #lemonTree

# 7. 문자열 나누기
str = "번호::이름::성적::성별::주소"
str = str.split("::")
print(str)  # ['번호', '이름', '성적', '성별', '주소']

# 8. 공백 지우기
str = "                 aaa "
print(str)
str = str.strip()
print(str)

