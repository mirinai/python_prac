import turtle as t

myT=None
myT=t.Turtle()#turtle모듈 안에 Turtle클래스 
myT.shape("turtle")

for _ in range(0,4):
    myT.forward(200)
    myT.right(90)
t.done()
#네모 그려짐(200x200)