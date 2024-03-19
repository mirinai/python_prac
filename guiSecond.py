from tkinter import *

window = Tk()
label1 = Label(window, text="python studying")
#fg : foreground(전경색)
label2 = Label(window, text="hard to study", font=("궁서체",30),
               fg="blue")
#bg : background
label3 = Label(window, text="python conquering",bg="magenta",width=20,height=5,anchor=SE)#
#anchor : 공간 안에 위치 채우기
#SE : southern east
label1.pack()#윈도우의 크기에 맞게 붙임
label2.pack()#윈도우의 크기에 맞게 붙임
label3.pack()#윈도우의 크기에 맞게 붙임

window.mainloop()


