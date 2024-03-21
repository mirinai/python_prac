from tkinter import *
from tkinter import messagebox

window = Tk()

#이벤트 핸들러 함수 정의
def myFunc():
    if chk.get()==0:
        #IndentationError: expected an indented block after 'if' statement on line 8
        messagebox.showinfo("체크버튼 exam","check button is turned off")
        print("chk :"+str(chk.get()))
    elif chk.get() == 1:
        messagebox.showinfo("check button exam", "check button is turned on")
        print("chk : "+str(chk.get()))
        

if __name__=="__main__":
    chk = IntVar()#IntVar() : 정수타입의 변수를 만듦
    cb1 = Checkbutton(window, text="클릭해라", variable=chk,command=myFunc)#
    
    cb1.pack()
    window.mainloop()
    
    