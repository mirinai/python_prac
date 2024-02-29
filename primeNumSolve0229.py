print("소수 구하기 프로그램")
n = int(input("소수를 구할 정수 한개 입력: "))
count_sosu = 0

for j in range(1,n+1):              # 1~n까지 j에 하나씩 넣어줌
    count_yaksu = 0
    for i in range(1,j+1):          # j의 약수가 몇갠지를 판단
        if j%(i) == 0:              # 1~j까지 나눠봐서 나머지가 0인 경우 약수갯수 +1
            count_yaksu +=1
        else :                      # 아니면 그냥 넘어가기
            pass
    if count_yaksu == 2:            # 약수가 두개면 소수
        print("%d은(는) 소수이다." % j)
        count_sosu += 1

print("1~%d 사이의 소수 개수 = %d" % (n,count_sosu))




