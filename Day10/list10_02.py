
names = ["김철수", "박민수", "이영희"]
score = [100, 85, 98]
age = [25, 23, 21]
end = False

while not end:
    print("*** 성적관리프로그램 ***")
    print("1. 등록")
    print("2. 검색")  # 부분조회
    print("3. 삭제")
    print("4. 조회")  # 전체조회
    print("5. 종료")
    print("**********************")
    sel = int(input("번호를 입력하세요 >>> "))
    if sel == 1:
        student_name = input("등록할 학생의 이름을 입력하세요 >>> ")
        names.append(student_name)
        student_score = input("위 학생의 성적을 입력하세요 >>> ")
        score.append(student_score)
        student_age = input("위 학생의 나이를 입력하세요 >>> ")
        age.append(student_age)
        print(student_name, "학생의 정보가 등록되었습니다.")

    elif sel == 2:
        search = input("검색할 학생의 이름을 입력하세요 >>> ")
        if search not in names:
            print("등록되지 않은 학생입니다.")
        else:
            i = 0
            while i < len(names):
                if search == names[i]:
                    print("성적 : ", score[i], ", 나이 : ", age[i])
                i += 1

    elif sel == 3:
        delete = input("삭제할 학생의 이름을 입력하세요 >>> ")
        if delete not in names:
            print("등록되지 않은 학생입니다.")
        else:
            i = 0
            while i < len(names):
                if delete == names[i]:
                    del[names[i]]
                    del[score[i]]
                    del[age[i]]
                    print("기록이 삭제되었습니다.")
                i += 1

    elif sel == 4:
        i = 0
        while i < len(names):
            print(i+1, "번 학생 ==> 이름 : ", names[i], ", 성적 : ", score[i], ", 나이 : ", age[i])
            i += 1

    elif sel == 5:
        print("프로그램을 종료합니다.")
        end = True
    else:
        print("잘못 입력했습니다.")