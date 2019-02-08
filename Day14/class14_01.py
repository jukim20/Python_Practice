def input_info2():
    global name, score, age, email, phone
    name.append(input("이름 "))
    score.append(int(input("성적 ")))
    age.append(int(input("나이 ")))
    email.append(input("이메일 "))
    phone.append(input("전화번호 "))


def input_info(name, score, age, email, phone):
    name.append(input("이름 "))
    score.append(int(input("성적 ")))
    age.append(int(input("나이 ")))
    email.append(input("이메일 "))
    phone.append(input("전화번호 "))
    return name, score, age, email, phone


def delete_info(name, score, age, email, phone):
    del_name = input("삭제할 이름을 입력하세요 >>> ")
    if del_name not in name:
        print("해당 이름을 가진 학생이 없습니다.")
    else:
        for i in range(len(name)):
            if del_name == name[i]:
                name.remove(del_name)
                del(score[i])
                del(age[i])
                del(email[i])
                del(phone[i])
                break
        return name, score, age, email, phone


name = ["park", "lee", "choi"]
score = [100, 97, 85]
age = [21, 25, 32]
email = ["aaa@aaa", "bbb@bbb", "ccc@ccc"]
phone = ["111-111", "222-222", "333-333"]
st_info = ["park", 100, 21, "aaa@aaa", "111-111"]
all_st_info = []
all_st_info.append(st_info)
st_count = len(name)

while True:
    print("** 학생 관리 프로그램 **")
    print("1. 등록")
    print("2. 삭제")
    print("3. 조회")
    print("4. 종료")
    sel = int(input("번호를 입력하세요 >>> "))
    if sel == 1:
        # all_info = input_info(name, score, age, email, phone)
        # name = all_info[0]
        # score = all_info[1]
        # age = all_info[2]
        # email = all_info[3]
        # phone = all_info[4]
        input_info2()
    elif sel == 2:  # 삭제는 이름으로 검사
        all_info = delete_info(name, score, age, email, phone)
        name = all_info[0]
        score = all_info[1]
        age = all_info[2]
        email = all_info[3]
        phone = all_info[4]

    elif sel == 3:
        for i in range(st_count + 1):
            print(name[i], " ", score[i], " ", age[i], " ", email[i], " ", phone[i])
    elif sel == 4:
        print("시스템이 종료됩니다.")
        break
    else:
        pass
