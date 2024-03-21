from tkinter import *
window = Tk()

b1=Button(window, text="button1")
b2=Button(window, text="button2")
b3=Button(window, text="button2")
'''
b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)
'''
b1.pack(side=RIGHT)
b2.pack(side=TOP)
b3.pack(side=BOTTOM)
window.mainloop()