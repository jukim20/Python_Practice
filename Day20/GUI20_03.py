from tkinter import *
"""
StringVar() : 문자열
IntVar() : 정수
DoubleVar() : 실수
BooleanVar() : 논리값 (True, False)
"""

win = Tk()
str1 = StringVar()
n1 = IntVar()
b1 = BooleanVar()
d1 = DoubleVar()  # 변수 매개가 만들어짐


def print_msg():
    str1.set("버튼1")  # str1 = '버튼1' ==> str1.set("버튼1")
    s1 = "버튼1"
    print("현재 클릭된 버튼 : ", str1.get())  # print(str) ==> print(str.get())


def print_msg2():
    str1.set("버튼2")
    s2 = "버튼2"
    print("현재 클릭된 버튼 : ", str1.get())


b1 = Button(win, text="버튼1", command=print_msg)  # print_msg() ==> command=print_msg  # 저 함수를 작동시켜라
b1.pack()

b2 = Button(win, text="버튼2", command=print_msg2)
b2.pack()


win.mainloop()