'''greeting = input("인삿말을 입력해 : ")#문자열로 받음

print("greeting = ",greeting)

print("greeting의 타입=",type(greeting))#greeting의 타입= <class 'str'>

print("greeting = %s"% greeting)

age = input("나이 입력 : ")
print("age의 타입 : ",type(age))
print("age : %s"%(age))#age : 25
#age=int(age)
'''
#age+=1
#print("age : %s"%(age))#    age+=1
#TypeError: can only concatenate str (not "int") to str
#age=age+"1";
#print("age : %s"%(age))#age : 241
'''age=int(age)

age=age+1
print("string to integer -> age : %d"%(age))#string to integer -> age : 26
print("string to integer -> age의 타입 : ",type(age))#string to integer -> age의 타입 :  <class 'int'>
'''
'''
print("원주율 파이값을 입력 : ",end=" ")#원주율 파이값을 입력 :  3.141592
pi = input()#
print("string pi = %s" % pi)#string pi = 3.141592
print("type of the pi : %s"% type(pi))#type of the pi : <class 'str'>
pi=float(pi)
print("pi = %f" % pi)#pi = 3.141592
print("type of the pi : ", type(pi))#type of the pi :  <class 'float'>
'''

'''
num=7
print("num=%d"% num)#num=7
print("num의 타입 : ",type(num))#num의 타입 :  <class 'int'>
num=str(num)
print("type of num : ",type(num))#type of num :  <class 'str'>
'''



