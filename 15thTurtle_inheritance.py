import turtle
import random
#부모 클래스
class Shape :
    myTurtle =None
    cx, cy =  0, 0#네모의 가운데좌표
    def __init__(self):
        self.myTurtle = turtle.Turtle("turtle")
    
    def setPen(self):
        r = random.Random()#0~1
        g = random.Random()
        b = random.Random()
        self.myTurtle.pencolor((r,g,b))
        pSize = random.randrange(1,10)
        self.myTurtle.pensize(pSize)
        
    def drawShape(self):
        pass

class Rectangle(Shape):#자식클래스
    width,height = [0]*2
    def __init__(self,x,y):
        #super().__init__()
        Shape.__init__(self)#위아래 둘 다 같음
        self.cx=x
        self.cy=y
        
    def drawShape(self):
        #실제로 거북이가 네모를 그리도록 하는 함수
        #return super().drawShape()
        pass
## 전역 함수 선언 ##
def screenLeftClick(x,y):
    rect = Rectangle(x,y)
    

if __name__=="__main__":
    turtle.title("거북이로 객체지향 네모를 그림")
    turtle.onscreenclick(screenLeftClick,1)#마우스 왼쪽버튼(1) 클릭하면 screenLeftClick함수 불러냄
    turtle.done()
    

