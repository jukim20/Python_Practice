# 문제 ) 성적 (0~100 ) 하나 입력받고 60이 넘으면 합격 이하면 불합격 출력
num = int(input("성적(0~100)을입력하세요 >>> "))
if num >= 60:
    print("합격")
else:
    print("불합격")
# 문제 ) 아이디와 비밀번호를 입력받고 로그인을 해보세요 . (로그인되었습니다 , 잘못입력했습니다)
db_id = "koreait"
db_pw = "12345"
# 문제 ) 거북이로 삼각형을 그려보세요
# 문제 ) 숫자를 입력받고 5의 배수이면서 3의 배수인지체크해보세요
if num % 5 == 0:
    print("5의배수")
# 문제 ) 짝수 홀수 를 구분하는 식을 만들어보세요 (응용)(힌트 : 나머지사용)
if num % 2 == 1:
    print("홀수")
import turtle as t  # as t  ==> turtle 은 이름이 길기때문에 t로 바꾼다
t.shape("turtle")
t.up()  # ==> 꼬리를 든다 ( 꼬리에 잉크가 묻어있어서 꼬리를 들면 선이 안그려진다 )
t.fd(100)
t.lt(20)
t.down()  # ==> 다시 꼬리를 내린다 (선이 그려진다 )
t.fd(200)
t.circle(200)  # ==> 원을 그린다.
t.exitonclick()
# 문제 1) 자기 이름중 한글자 거북이로 그려보세요~

