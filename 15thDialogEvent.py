from tkinter import *
from tkinter.simpledialog import *

if __name__=="__main__":
    window = Tk()
    window.geometry("400x100")
    label1 =Label(window,text="입력된 값=")
    label1.pack()
    
    value =askinteger("정수입력", "주사위 숫자(1~6)넣기 : ", minvalue=1,maxvalue=6)
    label1.configure(text="입력된 값 = "+str(value))
    window.mainloop()
    