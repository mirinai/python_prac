def test(a,b=10,c=100):
    print(a+b+c)
    sum=a+b+c
    return sum#return 키워드 : 함수를 실행했던 위치로 돌아가게 함
    print("---")


if __name__ =="__main__":
    hab = test(10,20,30)#60
    print("hab =", hab)
    hab = test(a=10,b=100,c=200)#310
    print("hab =", hab)
    hab = test(c=10,a=100,b=200)#310
    print("hab =", hab)
    hab = test(10,c=200)#220
    print("hab =", hab)
    hab = test(30)
    print("hab =", hab)




