#람다 함수 : 수식 형태로 되어 있어서 함수를 간편하게 작성 가능하며 함수를 한줄로 간단하게 만들어 줌
def hap(n1,n2):
    res=n1+n2
    return res

print("hap(10,20)=",hap(10,20))#hap(10,20)= 30
print("\n람다함수로 바꿈\n")

hap2 = lambda n1, n2 : n1+n2
print("hap2(30,40)=",hap2(30,40))#hap2(30,40)= 70

hap3 = lambda n1=20, n2=60 : n1+n2
print("hap3(90,60)=",hap3(90,80))#hap3(90,60)= 170
print("hap3()=",hap3())#hap3()= 80