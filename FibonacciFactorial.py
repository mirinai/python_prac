def fibonacci(n):
    
    if n ==1:
        return 1
    if n ==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
#fibonacci(3) = fibonacci(2)+fibonacci(1)
print("fibonacci(1) =",fibonacci(1))#fibonacci(1) = 1
print("fibonacci(2) =",fibonacci(2))#fibonacci(2) = 1
print("fibonacci(3) =",fibonacci(3))#fibonacci(3) = 2

print("fibonacci(4) =",fibonacci(4))#fibonacci(4) = 3
print("fibonacci(5) =",fibonacci(5))#fibonacci(5) = 5
print("fibonacci(6) =",fibonacci(6))#fibonacci(6) = 8
print("fibonacci(7) =",fibonacci(7))#fibonacci(7) = 13
print("fibonacci(8) =",fibonacci(8))#fibonacci(8) = 21


