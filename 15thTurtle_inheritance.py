import turtle
import random
#부모 클래스
class Shape :
    myTurtle =None#초기화
    cx, cy =  0, 0#네모의 가운데좌표
    def __init__(self):
        self.myTurtle = turtle.Turtle("turtle")
    
    def setPen(self):
        r = random.random()#0~1
        g = random.random()
        b = random.random()
        self.myTurtle.pencolor((r,g,b))
        pSize = random.randrange(1,10)
        self.myTurtle.pensize(pSize)
        
    def drawShape(self):
        pass

class Rectangle(Shape):#자식클래스
    width,height = [0]*2# 0두개를 만들어서 둘에 각각 넣음
    def __init__(self,x,y):
        #super().__init__()
        Shape.__init__(self)#위아래 둘 다 같음
        self.cx=x
        self.cy=y
        self.width=random.randrange(20,100)
        self.height=random.randrange(20,100)
        
        
    def drawShape(self):
        #실제로 거북이가 네모를 그리도록 하는 함수
        #return super().drawShape()
        #네모 그리기
        sx1,sy1,sx2,sy2=[0]*4
        sx1=self.cx - self.width/2
        sy1=self.cy - self.height/2
        #왼쪽 아래 점
        sx2=self.cx + self.width/2
        sy2=self.cy + self.height/2
        #오른쪽 위 점
        self.setPen()
        self.myTurtle.penup()#거북이 꼬리를 올림
        self.myTurtle.goto(sx1,sy1)
        self.myTurtle.pendown()#거북이 꼬리를 올림
        self.myTurtle.goto(sx1,sy2)
        self.myTurtle.goto(sx2,sy2)
        self.myTurtle.goto(sx2,sy1)
        self.myTurtle.goto(sx1,sy1)
        
        
## 전역 함수 선언 ##
def screenLeftClick(x,y):
    rect = Rectangle(x,y)
    rect.drawShape()
    

if __name__=="__main__":
    turtle.title("거북이로 객체지향 네모를 그림")
    turtle.onscreenclick(screenLeftClick,1)#마우스 왼쪽버튼(1) 클릭하면 screenLeftClick함수 불러냄
    turtle.done()#거북이 객체의 움짐임 끝내고 메모리에서 없앰
    

