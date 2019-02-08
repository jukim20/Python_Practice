from tkinter import*

# 엔트리 (ENTRY)
"""
1줄 짜리 간단한 텍스트 항목을 입력받을 때 사용한다.
"""
# 레이블 (LABEL)
"""
1줄 짜리 간단한 텍스트
"""

win = Tk()
win.title("로그인")  # Tk 에서 로그인으로 이름 바꿈

Label(win, text="아이디").grid(row=0)  # 한꺼번에 만든다
Label(win, text="비밀번호").grid(row=1)

e1 = Entry(win)
e2 = Entry(win)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

win.mainloop()
