def show_info(all_st_info):
    for i in range(len(all_st_info)):
        print("이름 : ", all_st_info[i][0], end=" , ")
        print("점수 : ", all_st_info[i][1], end=" , ")
        print("나이 : ", all_st_info[i][2], end=" , ")
        print("이메일 : ", all_st_info[i][3], end=" , ")
        print("전화번호 : ", all_st_info[i][4])


def add_info(all_st_info):
    st_info = []  # 비워주고 시작
    st_info.append(input("이름 >>> "))
    st_info.append(input("성적 >>> "))
    st_info.append(input("나이 >>> "))
    st_info.append(input("이메일 >>> "))
    st_info.append(input("전화번호 >>> "))
    all_st_info.append(st_info)
    return all_st_info

st_info = ["park", 100, 20, "aaa@aaa", "111-222"]
all_st_info = []
all_st_info.append(st_info)

while True:
    print("** 학생 관리 프로그램 **")
    print("1. 등록")
    print("2. 삭제")
    print("3. 조회")
    print("4. 종료")
    sel = int(input("번호를 입력하세요 >>> "))
    if sel == 1:
        all_st_info = add_info(all_st_info)
        print("정보가 등록되었습니다")

    elif sel == 2:  # 이름으로 삭제
        del_name = input("삭제할 학생의 이름을 입력하세요 >>> ")
        for i in range(len(all_st_info)):
            if del_name == all_st_info[i][0]:
                all_st_info[i].remove(del_name)
                print("해당 학생의 기록이 삭제되었습니다.")
                break
            elif del_name not in all_st_info[i][0]:
                print("잘못 입력했습니다.")

    elif sel == 3:
        show_info(all_st_info)

