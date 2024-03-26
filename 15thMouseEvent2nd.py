from tkinter import *
from tkinter import messagebox

def clickImage(event):
    messagebox.showinfo("마우스이벤트2","토끼그림에서 마우스가 클릭됨")

if __name__=="__main__":
    window=Tk()
    window.geometry("400x400")
    photo = PhotoImage(file="gif/rabbit.gif")
    label1=Label(window,image=photo)
    #label1.bind("<Button>",clickImage)#label1(사진)과 엮음
    window.bind("<Button>",clickImage)#window(GUI screen)와 엮음
    label1.pack(expand=True, anchor=CENTER)#윈도우 빈 이미지를 확장할 수 있음, label1을 가운데에 고정함
    window.mainloop()
    