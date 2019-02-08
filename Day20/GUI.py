from tkinter import *
"""
1. 레이아웃 메니저(배치관리자)(위치관리자)
    1) pack : 상하좌우
    2) grid : 행 열 
    3) place : 좌표
2. 옵션
    1) side : 시작위치 설정 (TOP , LEFT , RIGHT , BOTTOM)
    2) fill : 창에 가득차게 표시 (X, Y, BOTH)
    3) expand : 창의 크기가 변하면 위젯(객체통칭)의 배치도 비율대로 변함 YES , NO
    4) padx : 여백x
    5) pady : 여백y
    6) anchor : 위젯의 방위 따라 배치한다 (EWSN) (동서남북)
"""
win = Tk()  # tk 객체생성 (윈도우생성)
b1 = Button(win, text="버튼1")  # 객체 위치 , 내용
b1.pack()  # 위치 관리자 (1.pack)
b2 = Button(win, text="버튼2")
b2.pack(side=LEFT, fill=Y, padx=200, pady=300, expand=NO)

win.mainloop()  # 반복
