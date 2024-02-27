[a,b]=[10,20]
(c,d)=(10,20)
print("a =",a)
print("b =",b)
print("c =",c)
print("d =",d)
'''
a = 10
b = 20
c = 10
d = 20
'''
t=(10,20)
#튜플, 안의 값을 고칠수도 없고 없앨 수도 없음
print("t[0] =", t[0])#t[0] = 10
print("t[1] =", t[1])#t[1] = 20
#t[0]=25
#TypeError: 'tuple' object does not support item assignment(넣기)

t1=()#엘레멘트가 하나도  없는 빈 tuple
t2=(1,)#엘레멘트가 정수값 1 하나인 tuple t2=1, 로도 튜플 만들 수 있음 
print("type(t2) =",type(t2))#type(t2) = <class 'tuple'>
print("t2 =",t2)#t2 = (1,)
print()
t3=(1,2,3)
t4=1,2,3

print("type(t3) =",type(t3))
print("t3 =",t3)
'''
type(t3) = <class 'tuple'>
t3 = (1, 2, 3)
'''
print("type(t4) =",type(t4))#type(t4) = <class 'tuple'>
print("t4 =",t4)
'''
type(t4) = <class 'tuple'>
t4 = (1, 2, 3)
'''
print("t3[0]=%d, t3[2]=%d, t4[2]=%d"%(t3[0],t3[2],t4[2]))
#t3[0]=1, t3[2]=3, t4[2]=3
#del t3[2]
#TypeError: 'tuple' object doesn't support item deletion

#t4.append(8)
#AttributeError: 'tuple' object has no attribute 'append'

t6=(7,8,9)
t5 = t4+t6
print("t5 =",t5)#t5 = (1, 2, 3, 7, 8, 9)

t7=('a','b',("cd","fg"))

print("t7[1] =", t7[1])#t7[1] = b
print("t7[2] =", t7[2])#t7[2] = ('cd', 'fg')
print("t7[2][0] =",t7[2][0])#t7[2][0] = cd
print("t7[2][0] =",t7[2][1])#t7[2][0] = fg

print()
print("t7[1:3] =",t7[1:3])#t7[1:3] = ('b', ('cd', 'fg'))
print("t7[1: ] =",t7[1: ])#t7[1: ] = ('b', ('cd', 'fg'))\
print("t7[ :3] =",t7[ :3])#t7[ :3] = ('a', 'b', ('cd', 'fg'))
print("t7[ 0: ] =",t7[0: ])#t7[ 0: ] = ('a', 'b', ('cd', 'fg'))
print("t7[ : ] =",t7[ : ])#t7[ : ] = ('a', 'b', ('cd', 'fg'))
print()

t7 = t7+(5,)
print("5를 이은 뒤의 t7 =",t7)#5를 이은 뒤의 t7 = ('a', 'b', ('cd', 'fg'), 5)

tp2=(1,2,3,4,5)
#element찾기
print("3 in tp2 :", 3 in tp2)#3 in tp2 : True
print("7 in tp2 :", 7 in tp2)#7 in tp2 : False

print("7 not in tp2 :", 7 not in tp2)#7 not in tp2 : True
print()
print("tp2.index(3) =",tp2.index(3))#tp2.index(3) = 2
#3이라는 엘레멘트의 인덱스 리턴
tp2=(1,2,3,4,5,3)
print("tp2.index(3) =",tp2.index(3))#tp2.index(3) = 2
#첫번째 인덱스를 리턴한다
print("len(tp2) =",len(tp2))#len(tp2) = 6
tp2=(1,2,3,4,5,3,3,3)
print("tp2.count(3) =",tp2.count(3))#tp2.count(3) = 4
print("max(tp2) =",max(tp2))#max(tp2) = 5
print("min(tp2) =",min(tp2))#min(tp2) = 1

t9=('B','l','o','c','k')
for v in t9:
    print("v =",v)
'''
v = B
v = l
v = o
v = c
v = k
'''



