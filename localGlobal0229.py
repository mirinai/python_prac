def func():
    global a
    a=30#전역변수 a
    #a=10#지역변수
    print("func()안에서 a값 =%d"%a)
'''
지역 변수(local variable)
 함수 내에서 사용하는 변수(매개변수 포함) 
 함수에서 선언된 지역변수는 함수 내에서만 유효

 전역 변수(global variable)
 함수 외부에서 선언되는 변수
 메인 프로그램에서 선언되거나, 함수에서 global로 선언된
변수
 이러한 전역변수는 메인이나 함수에서 자유롭게 사용 가능

'''
def func2():
    print("func2()안에서 a값 =%d"%a)
#전역변수 a
a=20 # func함수 안에서 => 30
if __name__=="__main__":
    func()#func()안에서 a값 =10
    func2()#func2()안에서 a값 =20
    '''전역변수 선언한 뒤에 값
    func()안에서 a값 =30
    func2()안에서 a값 =30   
    '''


