from tkinter import *
from tkinter.filedialog import *

def func_open():
    fileName = askopenfilename(parent=window, filetypes=(("GIF파일","*.gif"),("모든 파일","*.*")))
    photo = PhotoImage(file=fileName)
    pLabel.configure(image=photo)
    pLabel.image = photo
    
def func_exit():
    window.quit()
    window.destroy()
    
if __name__=="__main__":
    window =Tk()
    window.geometry("400x400")
    window.title("명화 보기")
    
    photo = PhotoImage()
    pLabel = Label(window, image=photo)
    pLabel.pack(expand=True, anchor=CENTER)
    
    mainMenu=Menu(window)
    window.config(menu=mainMenu)
    
    fileMenu=Menu(mainMenu)
    mainMenu.add_cascade(label="파일", menu= fileMenu)
    fileMenu.add_command(label="파일 열기", command = func_open)
    fileMenu.add_separator()
    fileMenu.add_command(label="파일 닫기", command = func_exit)
    
    window.mainloop()