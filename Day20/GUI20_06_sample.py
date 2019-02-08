from tkinter import *
class App1:
    def __init__(self,win):
        self.n1 = IntVar()
        self.n2 = IntVar()
        self.sum = IntVar()
        Label(win, text="넘버1").grid(row=0, column=0)
        Label(win, text="넘버2").grid(row=1, column=0)
        Label(win, text="결과").grid(row=2, column=0)
        self.e1 = Entry(win, textvariable=self.n1)  # 엔트리에 적은내용이 변수에 저장된다.
        self.e1.grid(row=0, column=1)
        self.e2 = Entry(win, textvariable=self.n2)  # 엔트리에 적은내용이 변수에 저장된다.
        self.e2.grid(row=1, column=1)
        self.result = Entry(win, textvariable=self.sum)
        self.result.grid(row=2, column=1)
        self.b1 = Button(win, text="더하기", command=self.convet)
        self.b1.grid(row=2, column=2)
    def convet(self):
        a = self.n1.get()
        b = self.n2.get()
        c = a + b
        self.sum.set(c)
        print(a+b)
win = Tk()
app1 = App1(win)
win.mainloop()