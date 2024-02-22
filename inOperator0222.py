num=input("정수 하나 입력 :")
#스트링으로 받기

last = num[-1]#문자열의 마지막 끝에 있는 문자
print()
if last in "02468":#어느 리스트 안에 last의 값이 있으면 참
    print("num=%s는 짝수" % num)
elif last in "13579":
    print("num=%s는 홀수" % num)
else:
    print("잘못된 값")
print("\nclosing program")
print("\n-----------\n")



