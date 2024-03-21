from tkinter import *

btnList=[""]*9#elements : 9

fnameList=["eclair.gif","froyo.gif","gingerbread.gif","honeycomb.gif",
           "icecream.gif","jellybean.gif","kitkat.gif","lollipop.gif","marshmallow.gif"]


photoList=[None]*9
i,k=0,0
xPos, yPos = 0,0
num=0

if __name__=="__main__":
    window = Tk()
    window.geometry("210x210")
    for i in range(0,9):
        photoList[i]=PhotoImage(file="gif/"+fnameList[i])
        btnList[i]=Button(window, image=photoList[i])
    #num= 0, 1, 2, 3, 4
    #xPos = 0, 70, 140, 210, 0 ,70
    #yPos = 0, 70
    #i = 0, 1
    #k=0, 1
    
    
    for i in range(0,3):
        for k in range(0,3):
            btnList[num].place(x=xPos,y=yPos)
            num+=1
            xPos+=70
        xPos=0
        yPos+=70
    window.mainloop()
            