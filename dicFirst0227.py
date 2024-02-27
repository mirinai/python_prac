dic={'a':10,'b':20,'c':30,'d':40}
print("dic=",dic)#dic= {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print("dic['a']=",dic['a'])#dic['a']= 10
print("dic['d']=",dic['d'])#dic['d']= 40

print("type(dic)",type(dic))#type(dic) <class 'dict'>
print("dic.items()=",dic.items())#dic.items()= dict_items([('a', 10), ('b', 20), ('c', 30), ('d', 40)])

for key, value in dic.items():
    print("key:value = ",key,":",value,sep="")
'''
key:value = a:10
key:value = b:20
key:value = c:30
key:value = d:40
'''
for key in dic.keys():
    print("key=",key)
'''
key= a
key= b
key= c
key= d
'''
for val in dic.values():
    print("value =",val)
'''
value = 10
value = 20
value = 30
value = 40
'''
print("메서드들 한 뒤 dic =",dic)#메서드들 한 뒤 dic = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

data=dic.pop('a')
print("data=",data)#data= 10
print("dic.pop('a') 한 뒤 =",dic)#dic.pop('a') 한 뒤 = {'b': 20, 'c': 30, 'd': 40}
#pop : 리턴하고 없앰

basic=dic.pop("fruit","원소없음")
#"fruit"라는 키값이 없어서 뒤의 "원소없음"이 리턴
print("basic =",basic)#basic = 원소없음

dic={'a':10,'b':20,'c':30,'d':40,"fruit":"사과"}
basic=dic.pop("fruit","원소없음")
print("basic =",basic)#basic = 사과
#"fruit"의 value가 리턴 그리고 "fruit"없앰

print("마지막 dic =",dic)#마지막 dic = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
count=len(dic)
print("count =",count)#count = 4

del dic['c']#'c'를 없앰
print("'c'키 없앤 뒤의 dic =",dic)#'c'키 없앤 뒤의 dic = {'a': 10, 'b': 20, 'd': 40}
dic['b']=70
print("b키의 값을 바꾼 뒤의 dic =",dic)#b키의 값을 바꾼 뒤의 dic = {'a': 10, 'b': 70, 'd': 40}




