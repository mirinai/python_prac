lb = [[1,2,3],[4,5,6],[7,8,9]]#리스트 안의 리스트

print("li[0]=", lb[0])#li[0]= [1, 2, 3]
print("li[1]=", lb[1])#li[1]= [4, 5, 6]
print("li[2]=", lb[2])#li[2]= [7, 8, 9]

print()
print("li[0][0]=",lb[0][0])#li[0][0]= 1
print("li[0][1]=",lb[0][1])#li[0][1]= 2
print("li[0][2]=",lb[0][2])#li[0][2]= 3
print()
print("li[1][0]=",lb[1][0])#li[1][0]= 4
print()

print("lb를 매트릭스로 출력한 결과 :")
for i in range(0,len(lb),1):
    for j in range(0,len(lb[i]),1):
        print("%d"% lb[i][j],end=" ")
    print()

'''
lb를 매트릭스로 출력한 결과 :
1 2 3
4 5 6
7 8 9 : 
'''
print("\n-----------\n")
lc=[1,2,3]
lk=[4,5,6]
print("lc=",lc)#lc= [1, 2, 3]
print("lk=",lk)#lk= [4, 5, 6]
print("lc+lk=",lc+lk)#lc+lk= [1, 2, 3, 4, 5, 6]
#리스트들을 잇기

print("\n-----------\n")

#extend_뒤에 다른 리스트의 엘레멘트들을 넣음
lc.extend(lk)
print("lc.extend(lk)=",lc)#lc.extend(lk)= [1, 2, 3, 4, 5, 6]
print()
lc=[1,2,3]#초기화
listm=lc+lk
print("listm=",listm)#listm= [1, 2, 3, 4, 5, 6]
print()
print("lc*3=",lc*3)#lc*3= [1, 2, 3, 1, 2, 3, 1, 2, 3] lc를 세번 되풀이해라, * : repeat operator
print()
#길이
print("len(lc)=%d"% len(lc))#len(lc)=3
#리스트의 길이를 구할 수 있다
print()
#append : 뒤에 엘레멘트 넣기
lc.append(40)
lc.append(50)
print("lc=",lc)#lc= [1, 2, 3, 40, 50]
print()
#insert() : 넣고 싶은 위치에 엘레멘트 넣기
#insert(위치,엘레멘트)
lc.insert(0,-1)#0번째 인덱스의 자리에 -1을 넣고 뒤의 나머지는 뒤로 밀린다.
print("lc=",lc)#lc= [-1, 1, 2, 3, 40, 50]
print()
lc.insert(4,6.5)
print("lc=",lc)#lc= [-1, 1, 2, 3, 6.5, 40, 50]
print()

print("\n-----------\n")


