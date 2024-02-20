'''
A : 90~100
B : 80~89
C : 70~79
D : 60~69
F : 0~59

'''
score=int(input("input the score :"))

if (score>=90 and score<=100):# 90<= score <=100도 python에서는 됨
    print("A")
elif (score>=80 and score<90):
    print("B")
elif (score>=70 and score<80):
    print("C")
elif (60<= score <70):
    print("D")
elif (score>=0 and score<60):
    print("F")
else:
    print("잘못된 값이 입력됨")
print("closing program")
print("\n------------------")
if (score>=90 and score<=100):
    print("A")
elif (score>=80):
    print("B")
elif (score>=70):
    print("C")
elif (60<= score):
    print("D")
elif (score>=0):
    print("F")
else:
    print("잘못된 값이 입력됨")
print("closing program")
#/ : 몫이 아니라 실수로 구함
#// : 몫
print("\n------------------")
share=score//10
if (share==9 or share == 10):
    print("A")
elif (share==8):
    print("B")
elif (share==7):
    print("C")
elif (share==6):
    print("D")
elif (share<=5):
    print("F")
else:
    print("잘못된 값이 입력됨")
print("closing program")
print("\n------------------")
##홀수 아니면 짝수인지 

if score%2==0:
    print("score : %d\nscore은 짝수"%score)
else:
    print("score : %d\nscore은 홀수"%score)

#in operator

