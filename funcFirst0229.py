def print_3_times():
    print("hello")
    print("hello")
    print("hello")
def print_n_times(val,n):
    for i in range(n):
        print("val =", val)
'''
함수 = 특정 기능을 하는 코드들의 집합
     함수(Function) : ‘무엇’을 넣으면, ‘어떤 것’을 돌려주는 요술 상자
     메서드(Method)와 차이점 : 함수는 외부에 별도로 존재, 
메서드(method)는 클래스 안에 존재

함수를 호출
 함수 사용

매개변수(인자, 인수)
 함수 호출 시 괄호 내부에
넣는 여러 가지 자료

리턴값(반환값)
 함수를 호출하여 최종적으로
나오는 결
'''
val,n=input("돌릴 값, 갯수(띄어 써서 입력) :").split(" ")
n=int(n)
print_3_times()
print()
print_n_times(val,n)

'''
가변 매개변수(Variable Parameter)
– 함수의 매개변수로 전달되는 값들을 원하는 개수만큼 받을 수
있는 매개변수를 말함.
– 제약
• 가변 매개변수 뒤에 일반 매개변수가 와있는 함수인 경우 그
함수를 호출할 때는 일반 매개변수를 반드시 키워드 매개변수로
호출해야 함.
• 가변 매개변수는 하나만 사용할 수 있음
'''

