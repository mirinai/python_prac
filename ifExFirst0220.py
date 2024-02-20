a,b=4,8


if a < b:
    print("a is bigger than b")#a is bigger than b
elif a==b:
    print("a is same to b")#a is same to b
else:
    print("a is smaller than b")#a is smaller than b
print("closing program")#closing program

print("\n----------------")

num=input("정수 하나 입력 : ")#int(input())으로 많이 함
print("type of num :",type(num))#type of num : <class 'str'>
num=int(num)

##양수, 음수, 0인지 판단하는 조건문
if (num>0):
    print("num=%d is plus."% num)
elif(num==0):
    print("num=%d is zero."% num)
else:
    print("num=%d is minus."% num)

print("closing program")

