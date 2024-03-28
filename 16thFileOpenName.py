from tkinter import *
from tkinter.filedialog import *

if __name__=="__main__":
    window = Tk()
    window.geometry("400x400")
    label1=Label(window, text="선택된 파일 이름 : ")
    label1.pack()
    
    fileName=askopenfilename(parent=window, filetypes=(("GIF file","*.gif"), ("모든 파일","*.*")))
    label1.configure(text=str(fileName))
    window.mainloop()
    