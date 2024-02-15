print("train45".isalnum())#True

print("57".isdigit())#True

print("57".isalpha())#False

print("hello eeeeeeeee".find("hello"))#0

#오른쪽부터 찾음
print("hello hello".rfind("hello"))#6

print("-------------",end="\n\n")
#in 연산자 : 문자열내부에어떤문자열이있는지확인할때사용
#• 결과는True(맞다), False(아니다)로 출력

print("하이" in "하이 신시아")#True
print("terra" in "solar system")#False


print("-------------",end="\n\n")

#split() :
#문자열을특정한문자로자름
#리스트로 출력

#스페이스로 잘라냄
gul="10 20 30 40 50".split(" ")

print("gul의 출력 : ",gul)#gul의 출력 :  ['10', '20', '30', '40', '50']
#문자열로 되어있는 리스트


#gul1=map(int,input().split(" ")) 입력할 때에는 이렇게 많이 씀

print("terra"[2])#r 0->t, 1->e, 2->r ....

print("gul의 타입,",type(gul))#gul의 타입, <class 'list'>

m="a,b,c,d,e".split(",")
print("m 출력 : ",m)#m 출력 :  ['a', 'b', 'c', 'd', 'e']
#문자를 받은 리스트

print("-------------",end="\n\n")

#Boolean : True, False만 가질 수 있다.

#비교연산자로 만듦 exam) ==,!=,>,<.....


a=4
b=7 #a, b = 4, 7
print("a==b : ",a==b)#a==b :  False
print("a!=b : ",a!=b)#a!=b :  True
a,b=7,7
print("a>b :",a>b)#a>b : False
print("a==b :",a==b)#a==b : True





