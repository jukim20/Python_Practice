#  grid 관리자
"""
row : 행 번호
column : 열 번호
rowspan : 행의 갯수
columnspan : 열의 갯수
padx : 여백
pady : 여백
stick : 경계 맞춤 (EWSN)
"""

from tkinter import *

win = Tk()  # 윈도우 객체생성
b1 = Button(win, text="버튼1")
b1.grid(row=0, column=0, padx=10, pady=10)
b2 = Button(win, text="버튼2")
b2.grid(row=1, column=0, padx=10, pady=10)
b3 = Button(win, text="버튼3")
b3.grid(row=0, column=1)
b4 = Button(win, text="버튼4")
b4.grid(row=1, column=1)

win.mainloop()  # 반복 (루프)
