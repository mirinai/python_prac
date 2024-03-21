from tkinter import *
from tkinter import messagebox


##이벤트 핸들러 함수 정의
def btEventFunc():
    messagebox.showinfo("강아지 버튼","강아지가 귀엽다")

if __name__=="__main__":
    Window = Tk()
    photo = PhotoImage(file="gif/cat2.gif")
    b1 = Button(Window, image=photo, command=btEventFunc)#()없어도 됨
    b1.pack()
    Window.mainloop()
    
    
    