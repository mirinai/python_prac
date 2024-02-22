num=[10,20,"apple",True,3.14]

print("num의 타입 :",type(num))#num의 타입 : <class 'list'>
print("num=",num)#num= [10, 20, 'apple', True, 3.14]

print("num[0]=%d" % num[0])#num[0]=10
print("num[1]=%d" % num[1])#num[1]=20
print("num[2]=%s" % num[2])#num[2]=apple
print("num[3]=",num[3])#num[3]= True
print("num[4]=%.2f" % num[4])#num[4]=3.14
print()
print("num[2][0]=%c"%num[2][0])#num[2][0]=a /num[2]은 하나의 리스트, 리스트안의 리스트의 첫 엘레먼트
print("num[2][1]=%c"%num[2][1])#num[2][1]=p, 리스트안의 리스트의 둘째 엘레먼트
print("num[2][2]=%c"%num[2][2])#num[2][2]=p
print("num[2][3]=%c"%num[2][3])#num[2][3]=l
print("num[2][4]=%c"%num[2][4])#num[2][4]=e
print("\n-----------\n")

print("num[-1]",num[-1])#num[-1] 3.14
print("num[-3]",num[-3])#num[-3] apple

print("\n-----------\n")

print("slicing 연산")
print("num[0:3]=",num[0:3])#num[0:3]= [10, 20, 'apple']
#3번째 엘레멘트들까지 출력됨, 4번째[3]은 안됨
print("num[ :3]=",num[ :3])#num[ :3]= [10, 20, 'apple']
#0부터 출력함
print("num[2:5]=",num[2:5])#num[2:5]= ['apple', True, 3.14]
print("num[2: ]=",num[2: ])#num[2: ]= ['apple', True, 3.14]
#인덱스 2번 엘레멘트부터 끝까지 출력
print("num[ : ]=",num[ : ])#num[ : ]= [10, 20, 'apple', True, 3.14]
#다 출력




