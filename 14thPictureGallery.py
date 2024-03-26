from tkinter import *
from time import *

#전역변수 선언 파트
fNameList=["jeju1.gif","jeju2.gif","jeju3.gif",
           "jeju4.gif","jeju5.gif","jeju6.gif","jeju7.gif","jeju8.gif","jeju9.gif",]

photoList=[None]*9
num = 0

def clickNext():
    global num 
    num+=1
    if num>8:
        num=0
    photo = PhotoImage(file="gif/"+fNameList[num])
    pLabel.configure(image=photo)
    pLabel.image=photo
def clickPrev():
    global num 
    num-=1
if __name__=="__main__":
    window=Tk()
    window.geometry("700x500")
    window.title("seeing picture album")
    btnPrev = Button(window, text="<<이전",command=clickPrev)
    btnNext = Button(window, text="다음>>",command=clickNext)
    
    photo = PhotoImage(file="gif/"+fNameList[0])
    pLabel = Label(window, image=photo)
    
    btnPrev.place(x=250,y=10)
    btnNext.place(x=400,y=10)
    pLabel.place(x=15,y=50)
    window.mainloop()