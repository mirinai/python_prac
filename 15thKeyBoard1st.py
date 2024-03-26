from tkinter import *
from tkinter import messagebox

def keyEvent(event):
    messagebox.showinfo("키보드 이벤트","눌린 키 : "+chr(event.keycode))#아스키코드를 문자로 바꿈
    print("event.keycode = %d" % event.keycode)

if __name__=="__main__":
    window = Tk()
    #window.bind("<Key>", keyEvent)#<key> : 모든 키
    #window.bind("<Return>",keyEvent)#enter키만 처리함,event.keycode = 13
    #window.bind("<BackSpace>",keyEvent)#back space키만 처리함,event.keycode = 8
    window.bind("<space>",keyEvent)#space키만 처리함, event.keycode = 32, 소문자로 해야함
    
    
    
    window.mainloop()