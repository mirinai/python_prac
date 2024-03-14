def fact(n):
    if n == 0:
        return 1#함수 불러내기가 안되니까 그대로 리턴
    else:
        return n * fact(n-1)#리턴이 아니라 함수 불러내기
    

print("1!=",fact(1))#1!= 1
print("2!=",fact(2))#2!= 2
print("3!=",fact(3))#3!= 6
print("4!=",fact(4))#4!= 24
print("5!=",fact(5))#5!= 120


