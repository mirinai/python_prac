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
def print_n_times(n,*val):#가변 매개변수(Variable Parameter)
    print("type(val) =",type(val))#type(val) = <class 'tuple'>
    for i in range(n):
        for data in val:
            print("data =", data,end="|")
        print()

print_n_times(3,"hello","world","python")
print("\n\n-----------------\n")

#기본 매개변수(default parameter)
#매개변수의 값을 입력하지 않았을 경우 매개변수에
#들어가는 기본값

#기본 매개변수가 가변 매개변수보다 앞에 올 때
#기본 매개변수의 의미가 사라짐

#가변 매개변수가 기본 매개변수보다 앞에 올 때
#– 가변 매개변수가 우선됨

def disp(val,n=2):
    for i in range(n):
        print("val-%s" %val)

def show_n_times(*val,n=2):
    print("type(val) =",type(val))#type(val) = <class 'tuple'>
    for i in range(n):
        for data in val:
            print("data =", data,end="|")
        print()

def write_n_times(*val,n):
    print("type(val) =",type(val))#type(val) = <class 'tuple'>
    for i in range(n):
        for data in val:
            print("data =", data,end="|")
        print()

if __name__ == "__main__":#모듈에 if __name__=="__main__"이라는 조건문을 넣어주고 그 아래는 직접 실행시켰을 때만 실행되길 원하는 코드들을 넣어주는 것으로 생각하면 쉬울 것이다.
    print_n_times(2,"hello","world","python")
    disp("hi",3)
    '''
    val-hi
    val-hi
    val-hi
    '''
    print()
    disp("hi")
    '''
    val-hi
    val-hi
    '''
    show_n_times("hello","world","python",2)
    print("\n\n-----------------\n")
    #키워드 매개변수(Keyword parameter)

    write_n_times("are you okay","hi","hello",n=2)#키워드 parameter
    write_n_times("are you okay","hi","hello",n=2)
'''
type(val) = <class 'tuple'>
data = are you okay|data = hi|data = hello|
data = are you okay|data = hi|data = hello|
'''

    
    
    
    
