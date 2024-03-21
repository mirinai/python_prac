from tkinter import *

window = Tk()

#이벤트 핸들러 함수 정의
def myFunc():
    if var.get()==1:
        label1.configure(text="Python")
        print("var.get()=%d"%var.get())
    elif var.get()==2:
        label1.configure(text="C++")
        print("var.get()=%d"%var.get())
    elif var.get()==3:
        label1.configure(text="JAVA")
        print("var.get()=%d"%var.get())
if __name__=="__main__":
    var = IntVar()
    rb1 = Radiobutton(window, text="Python", variable=var, value=1,command=myFunc)#Python을 고르면 var에 value의 값을 넣겠다.
    rb2 = Radiobutton(window, text="C++", variable=var, value=2,command=myFunc)
    rb3 = Radiobutton(window, text="JAVA", variable=var, value=3,command=myFunc)
    label1 =Label(window, text="고른 언어 : ", fg="red")
    rb1.pack()
    rb2.pack()
    rb3.pack()
    label1.pack()
    window.mainloop()
    