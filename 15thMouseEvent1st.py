from tkinter import *
from tkinter import messagebox

#전역 함수 선언
def clickLeft(event):
    messagebox.showinfo("마우스 이벤트","마우스 왼쪽버튼이 클릭됨")

def clickRight(event):
    messagebox.showinfo("마우스 이벤트","마우스 오른쪽 버튼이 클릭됨")
    
if __name__=="__main__":
    window = Tk()
    window.bind("<Button-1>",clickLeft)#<Button-1> : 마우스 왼쪽버튼 이벤트 코드
    #<Button> : 모든 마우스 버튼 이벤트 코드
    window.bind("<Button-3>",clickRight)#<Button-3> : 마우스 왼쪽버튼 이벤트 코드
    window.mainloop()
    
    
    