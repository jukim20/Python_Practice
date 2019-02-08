def input_info2():
    global name, score, age, email, phone
    name = input("이름")
    score = int(input("성적"))
    age = int(input("나이"))
    email = input("이메일")
    phone = input("전화번호")
def input_info(name, score, age, email, phone):
    name.append(input("이름 "))
    score.append(int(input("성적 ")))
    age.append(int(input("나이 ")))
    email.append(input("이메일 "))
    phone.append(input("전화번호 "))
    return name, score, age, email, phone
name = ["park", "lee", "choi"]
score = [100, 200, 300]
age = [20, 21, 25]
email = ["aaa@aaa", "bbb@bbb", "ccc@ccc"]
phone = ["111-111", "222-222", "333-333"]
while True:
    print("** 학생 관리 프로그램 **")
    print("1. 등록")
    print("2. 삭제")
    print("3. 조회")
    print("4. 종료")
    sel = int(input("번호를 입력하세요 >>> "))
    if sel == 1:
        all_info = input_info(name, score, age, email, phone)
        name = all_info[0]
        score = all_info[1]
        age = all_info[2]
        email = all_info[3]
        phone = all_info[4]
        #  input_info2()
    elif sel ==2:pass  # 삭제는 이름으로 검사
    elif sel ==3:
        for i in range(len(name)):
            print(i + 1, " ", name[i], " ", score[i], " ", age[i], " ", email[i], " ", phone[i])
        # print(name, " ", score, " ", age, " ", email, " ", phone)
