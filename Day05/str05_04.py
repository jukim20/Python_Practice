import datetime  # 날짜관련
today = datetime.date.today()
print(today)  # 2018-03-16
# print(today[0])  # TypeError: 'datetime.date' object is not subscriptable
str1 = "korea"
print(str1[0])  # k
# type(자료형) ==> 자료형의 현재 type 을 알려준다
print(type(str1))  # <class 'str'>
num = 10
print(type(num))  # <class 'int'>
print(type(today))  # <class 'datetime.date'>
#  타입변환(casting)
today = str(today)
print(type(today))  # <class 'str'>
print(today)  # 2018-03-16
#  문제1) today 를 슬라이싱해서 2018년03월16일 을 출력하세요
# today = "2018년03월16일"
yy = today[0:4]
mm = today[5:7]
dd = today[8:10]
today = yy + "년" + mm + "월" + dd + "일"
print(today)
#  문제 2) 주민번호를 입력받고 , 남자 인지 여자인지 출력
jumin = "880320-2628847"
if jumin[7] == "1":
    print("남자")
elif jumin[7] == "2":
    print("여자")
#  문제 3) 주민번호를 입력받고  나이 출력 , 생일 출력

