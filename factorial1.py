def fact(n):
    output = 1
    for i in range(1,n+1):
        output *= i
    return output

print("1!=",fact(1))#1!= 1
print("3!=",fact(3))#3!= 6
print("4!=",fact(4))#4!= 24
print("5!=",fact(5))#5!= 120
