def show_info(all_st_info):
    for i in range(len(all_st_info)):
        print("이름 :", all_st_info[i][0], end=" , ")
        print("점수 :", all_st_info[i][1], end=" , ")
        print("나이 :", all_st_info[i][2], end=" , ")
        print("이메일 :", all_st_info[i][3], end=" , ")
        print("전화번호 :", all_st_info[i][4])
def add_info(all_st_info):
    st_info = []
    # name = input("이름")
    # st_info.append(name)
    st_info.append(input("이름"))
    st_info.append(input("성적"))
    st_info.append(input("나이"))
    st_info.append(input("이메일"))
    st_info.append(input("전화번호"))
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
    elif sel == 2:
        name = input("삭제할 이름을 입력하세요")

        for i in range(len(all_st_info)):
            if name == all_st_info[i][0]:
                all_st_info.remove(all_st_info[i])
                break
            elif name not in all_st_info[i][0]:
                print("이름을 잘못 입력했습니다 ")
    elif sel == 3:
        show_info(all_st_info)
