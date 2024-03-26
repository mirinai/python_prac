from tkinter import *
from tkinter import messagebox
def func_open():
    messagebox.showinfo("열기메뉴선택","열기 메뉴를 고름")
def func_exit():
    window.quit()
    window.destroy()#메모리에서도 지움
if __name__=="__main__":
    window = Tk()
    mainMenu = Menu(window)#우리가 만든 윈도우에 메뉴 만들기
    window.config(menu = mainMenu)
    
    fileMenu =Menu(mainMenu)#메인메뉴에 들어갈 파일메뉴
    mainMenu.add_cascade(label="파일", menu=fileMenu)#폭포처럼 넣기
    fileMenu.add_cascade(label="열기", command=func_open)#func_open를 불러내라
    fileMenu.add_separator()#구분선
    fileMenu.add_command(label="인쇄")
    fileMenu.add_separator()#구분선
    fileMenu.add_command(label="종료", command=func_exit)#func_exit를 불러내기
    
    
    window.mainloop()
    