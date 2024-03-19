import turtle as t
import random as rd
#이벤트핸들함수
def screenLeftClick(x,y):
    global r,g,b
    t.pencolor((r,g,b))
    t.pendown()#꼬리내림,그리기시작
    t.goto(x,y)#클릭한 곳의 x,y좌표가 넘어감
    
    
#전역변수 선언
pSize=10
r, g, b = 1.0, 0.0, 0.0

t.title("거북이로 그린 그림")
t.shape("turtle")
t.pensize(pSize)
#콜백함수
t.onscreenclick(screenLeftClick, 1)#캔버스에 마우스 왼쪽버튼을 클릭하면, (함수불러냄,1 : 마우스 왼쪽 버튼)
t.done()