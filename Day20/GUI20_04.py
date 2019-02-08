from tkinter import *


class App1:
    # def init(self, win):
    #     self.b1 = Button(win, text="종료2", command=win.quit)
    #     self.b1.pack()
    #     self.b1["fg"] = "red"  # 글자색 레드로 변경
    #     self.b1["bg"] = "yellow"  # 버튼 배경색 노랑으로 변경
    #     self.b1["font"] = "Times", 110, "bold"  # 글씨체 변경

    def __init__(self, win):  # 처음에 한 번 자동으로 실행된다
        self.b1 = Button(win, text="종료2", command=win.quit)
        self.b1.pack()
        self.b1["fg"] = "red"  # 글자색 레드로 변경
        self.b1["bg"] = "yellow"  # 버튼 배경색 노랑으로 변경
        self.b1["font"] = "Times", 110, "bold"  # 글씨체 변경


win = Tk()
b1 = Button(win, text="종료1", command=win.quit)  # 내부적으로 저장되어있는 함수
b1.pack()
# app1 = App1()  # 1번 방법
# app1.init(win)

app1 = App1(win)  # 2번 방법  # 처음에 한 번 자동으로 실행된다

# 문제 1) 출력 함수를 만들어보자


# 문제 2)

win.mainloop()