#range(0,4,1)
print("range(0,4,1)=",list(range(0,4,1)))#range(0,4,1)= [0, 1, 2, 3]
print()
print("range(0,4)=",list(range(0,4)))#range(0,4)= [0, 1, 2, 3]
#기본적으로 1씩 올라감
print()
print("range(4)=",list(range(4)))#range(0,4)= [0, 1, 2, 3]
#기본적으로 0에서 시작함

print("range(0,11,2)=",list(range(0,11,2)))#range(0,11,2)= [0, 2, 4, 6, 8, 10]
#11앞까지 2씩 늘어남
print("\n---------------\n")

n=1
sum=0
sum=n+sum #sum=1
n+=1#n=2
sum=sum+n#sum=3
n+=1#n=3
sum=sum+n#sum=6
n+=1#n=4
sum=sum+n#sum=10
print("sum=%d"%sum)#sum=10
#.
#.
#.
#되풀이해서 1~n값까지 더해서 sum을 조금씩 높이는 원리
print("\n---------------\n")
n=1 #2, 3, 4, 5
sum=0#1, 3, 6, 10
for n in range(1,5,1):#n = 1,2,3,4
    sum+=n#sum=sum+n
    #n=n+1
    print("n=%d, sum=%d"%(n,sum))
    '''
    n=1, sum=1
    n=2, sum=3
    n=3, sum=6
    n=4, sum=10
    '''

print("\nfor에서 나온 뒤의 sum =%d, n=%d"%(sum,n))#for에서 나온 뒤의 sum =10, n=5
print("\nlist로 레인지를 갈았을 때\n")
sum=0
for n in [1,2,3,4]:
    sum+=n#sum=sum+n
    #n=n+1
    print("n=%d, sum=%d"%(n,sum))
    '''
    n=1, sum=1
    n=2, sum=3
    n=3, sum=6
    n=4, sum=10
    '''

print("\nfor에서 나온 뒤의 sum =%d, n=%d"%(sum,n))#for에서 나온 뒤의 sum =10, n=5




