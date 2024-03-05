'''
제너레이터와 yield
- yield 문 : 함수를 종결하지 않으면서 값을 계속 반환

'''

def getFunc1():
    yield 1
    yield 2
    yield 3
def getFunc2(num):
    for i in range(0,num):
        yield i
        print("generator 하고 있음")

print(list(getFunc1()))#[1, 2, 3]

print()

for data in getFunc2(5):
    print(data)
'''
0
generator 하고 있음
1
generator 하고 있음
2
generator 하고 있음
3
generator 하고 있음
4
generator 하고 있음'''

'''
제너레이터(Generator : 생성자) 함수 : yield가 포함된 함수
• yield 문으로 값을 반환한 후 계속 진행

내부 함수 
- 내부 함수 : 함수 안에 함수가 있는 형태

'''



