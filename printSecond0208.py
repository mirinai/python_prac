print("3 + 4 =",3+4,sep=" ")
a =7;
b=5;
print("정수 7=%d"%(a+b))
#print("a=",a)  #주석(comment)기호
#print("b=",b)
print("정수 {} = {} + {}".format(a+b,a,b))
'''아아아'''
print("a=",a,"b=",b)
print("a=%d"%a)#서식지정자
print("b=%d"%b)
print("a : %d, b : %d"%(a,b))

print(".format -> a : {}, b : {}".format(a,b))
'''% : place holder
   d  : devimal Number -> 10진수 서식으로 써라'''
print("a + b =",end=" ")
print(a+b)
print("------------------------------")

'''
%d : 10진수 정수
%x : 16진수 정수 Hexa Decimal Number
%o : 8진수 
%f : 실수 floating point number
%c : 한글자 character
%s : 문자열 string
'''
print("혈액형 : %c"%'A')
#print("유니코드 : %d"%"A") 파이썬에서는 chr() ord()로 아스키코드나 문자로 바꿈
print("이름 : %s"%("내이름"))
age=27
print("age=%5d"%age)#age=   27 오른쪽 정렬
print("age=%05d"%age)#age=00027 빈자리는 0
print("age=%-5d"%age)#age=27 왼쪽정렬
pi=3.14159265
print("pi=",pi)#pi= 3.14
print("pi : %d"%pi)#pi : 3
print("pi : %f"%pi)#pi : 3.141593 : 반올림 됨
print("pi : %.2f"%pi)#pi : 3.14

