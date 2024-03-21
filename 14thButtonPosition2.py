from tkinter import *
window = Tk()

btnList=[""]*3#btnList = ["","",""]

for i in range(0,3):
    btnList[i] = Button(window, text="Button "+str(i+1))

'''for btn in btnList:
    btn.pack(side=TOP, fill = X,padx=10,pady=10)'''
    
for btn in btnList:
    btn.pack(side=TOP, fill = X,ipadx=10,ipady=10,padx=10,pady=10)# i : 안의 패드




window.mainloop()