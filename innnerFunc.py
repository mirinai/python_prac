'''내부 함수 
- 내부 함수 : 함수 안에 함수가 있는 형태'''

def outFunc(v1, v2):
    def inFunc(n1,n2):
        return n1+n2
    return inFunc(v1,v2)

print(outFunc(10,20))#30
'''
- outFunc() 함수 밖에서 내부함수를 호출하면 오류 발생

'''
'''
 지역 변수(local variable)
 함수 내에서 사용하는 변수(매개변수 포함) 
 함수에서 선언된 지역변수는 함수 내에서만 유효

 전역 변수(global variable)
 함수 외부에서 선언되는 변수
 메인 프로그램에서 선언되거나, 함수에서 global로 선언된 변수
 이러한 global 키워드를 사용하여서 함수 안에서 전역변수를 사용 가능

 yield 문
 함수를 종결하지 않으면서 값을 계속 반환
 제너레이터(Generator : 생성자) 함수
 yield가 포함된 함수
 내부 함수 : 함수 안에 함수가 있는 형태
'''


