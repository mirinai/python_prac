from tkinter import *
from tkinter.filedialog import *

if __name__=="__main__":
    window = Tk()
    window.geometry("400x400")
    label1=Label(window, text="넣은 파일 이름 : ")
    label1.pack()
    
    saveFP=asksaveasfile(parent=window, mode="w",defaultextension=".jpg", filetypes=(("JPG file","*.jpg;*.jpeg"), ("모든 파일","*.*")))
    label1.configure(text=str(saveFP))
    saveFP.close()
    window.mainloop()
    