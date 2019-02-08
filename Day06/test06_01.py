# ================================== 복습 ====================================

# 문제 ) 성적을 하나 입력 받고 100~91 ==> A, 90~81 ==> B, 이하 재시험 (논리연산자 사용)

grade = int(input("성적을 입력하세요 >>> "))

if grade < 0 or grade > 101:
    print("잘못 입력했습니다.")
elif grade < 100:
    if grade >= 91:
        print("A")
    elif grade >= 81:
        print("B")
    else:
        print("재시험")
# ============================================================================
# 문제 ) 주민번호를 입력받고, 남자인지 여자인지 출력

ssn = input("주민번호를 입력하세요 (- 를 포함하세요.) >>> ")

if len(ssn) == 14:
    if ssn[7] == "1" or ssn[7] == "3":
        print("남성입니다.")
    elif ssn[7] == "2" or ssn[7] == "4":
        print("여성입니다.")
    else:
        print("잘못 입력했습니다.")
else:
    print("잘못 입력했습니다.")

# 문제 ) korea, it 만 출력
str2 = "korea it"
print(str2[0:5] + str2[6:8])

# 문제 ) 숫자를 입력받고 5 의 배수이면서 3 의 배수인지 체크해보세요.
num = int(input("숫자를 입력하세요 >>> "))

if num % 5 == 0 and num % 3 == 0:
    print("True")
else:
    print("False")

# 문제 ) 아이디와 비밀번호를 입력받고 로그인을 해보세요. (로그인 되었습니다, 잘못 입력했습니다)
db_id = "koreait"
db_pw = "12345"

id = input("아이디를 입력해세요 >>> ")
pw = input("비밀번호를 입력하세요 >>> ")

if id == db_id:
    if pw == db_pw:
        print("로그인 되었습니다.")
    else:
        print("비밀번호를 잘못 입력했습니다.")
else:
    print("아이디를 잘못 입력했습니다.")
