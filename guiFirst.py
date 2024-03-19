from tkinter import *
'''
• Tcl/Tk를 파이썬에서 사용할 수 있도록 인터페이스하는 모듈
• 파이썬에 내장'''
window = Tk()


#• 타이틀 바, 경계선, 출력 표면 가진 메인 윈도우 생성
window.title("윈도우 창 연습")
window.geometry("400x100")
window.resizable(width=TRUE, height=TRUE)#마우스로 크기 조절할 수 있음
window.resizable(width=FALSE, height=False)

window.mainloop()#GUI 툴킷으로 크로스 플랫폼 지원