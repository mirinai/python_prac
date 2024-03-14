counter=0
def fibonacci(n):
    print("fibonacci ({})를 구하기".format(n))
    global counter#위의 가운터 변수를 가져다 쓰겠다.
    counter+=1
    if n ==1:
        return 1
    if n ==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
#fibonacci(3) = fibonacci(2)+fibonacci(1)

print("fibonacci(10) =",fibonacci(10))#fibonacci(10) = 55
print("-----")
print("fibonacci(10)의 덧셈은 {}번".format(counter))#fibonacci(10)의 덧셈은 109번