# 문자열 인덱싱 ( 문자열은 글자수대로 방이 만들어지고 한글자씩 저장된다)
# 저장된후 방번호를 붙여준다 ==> (인덱스 (index))
# 방번호(인덱스) 는 0번부터 시작한다
# 인덱스를 이용해서 한칸한칸씩 접근이 가능하다
# 사용법 ==> 변수[인덱스]
# 뒤에서 부터는 -1 로 시작한다.
str1 = "헬로우월드"
print(str1)
print(str1[0])
print(str1[4])
print(str1[-1])  # 드
print(str1[-3])  # 우
# print(str1[5])  # IndexError: string index out of range
# 문자열 슬라이싱(인덱싱의 범위)
str2 = "korea it"
print(str2)  # korea it
print(str2[1:4])  # ore  ==>    1 <=   < 4
# 문제 )  korea , it











