'''
print("소수구하기 프로그램")
num=int(input("소수를 구할 정수 하나 넣기 : "))
count=0

i = 2  
while i <= num:
    isosu = True  
    for j in range(2, int(i ** 0.5) + 1):  
        if i % j == 0:
            
            isosu = False
            break
    if isosu:
        print("%d는 소수입니다." % i)
        count += 1
    i += 1

print("1~%d사이의 소수의 개수 : %d"%(num,count))
'''
print("에라토스테네스의 체를 활용한 소수 구하기 프로그램")
num = int(input("소수를 구할 정수 하나 넣기: "))

# 소수를 저장할 리스트를 초기화합니다.
prime = [True] * (num + 1)
prime[0] = prime[1] = False  # 0과 1은 소수가 아닙니다.

# 에라토스테네스의 체 알고리즘을 사용하여 소수를 구합니다.
for i in range(2, int(num ** 0.5) + 1):
    if prime[i]:
        for j in range(i * i, num + 1, i):#소수인 n의 배수를 거짓
            prime[j] = False

# 소수를 출력하고 개수를 세기 위한 변수를 초기화합니다.
count = 0
print("1~%d 사이의 소수:" % num, end=" ")
for i in range(2, num + 1):
    if prime[i]:#소수라면 

        print(i, end=" ")#출력
        count += 1#소수 세기


print("\n1~%d 사이의 소수의 개수: %d" % (num, count))
