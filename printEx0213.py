print("10진수 13 = %d"% 13)
print("16진수 13 = %X"% 13)
print("16진수 13 = %x"% 13)
''' 10진수 13 = 13
    16진수 13 = D
    16진수 13 = d'''
print("16진수 25 = %X" % 25)#16진수 25 = 19
print("16진수 29 = %X"% 29)#16진수 29 = 1D
print("16진수 45 = %X"% 45)#16진수 45 = 2D
print()
print("8진수 13 = %o"% 13)#8진수 13 = 15
print("파이 = %f" % 3.141592)#파이 = 3.141592
print("문자열 타입 = ", type("안녕"))#문자열 타입 =  <class 'str'>
print("정수 75=", type(75))#정수 75= <class 'int'>
print()
print("반갑다 라고 말했음.")#반갑다 라고 말했음.
print('"반갑다" 라고 말했음.')#"반갑다" 라고 말했음.
print("'반갑다' 라고 말했음.")#'반갑다' 라고 말했음.
print()
print("\"반갑다\" 라고 말했음.")#"반갑다" 라고 말했음.
print("\'반갑다\'라고 말함")#'반갑다'라고 말함
print("인천시\n미추홀구\t학익동\nInha University")
print("지금은 2월달")#print는 기본적으로 엔터쳐줌 print()==print(end="\n")
'''
인천시
미추홀구        학익동
Inha University
지금은 2월달
'''
print("\"반갑다\" 라고 말했음.")#"반갑다" 라고 말했음.
print("\'반갑다\'라고 말함")#'반갑다'라고 말함
print("인천시\n미추홀구\t학익동\nInha University",end="\n")
print("지금은 2월달")
'''
"반갑다" 라고 말했음.
'반갑다'라고 말함
인천시
미추홀구        학익동
Inha University
지금은 2월달
'''
print()
print("지금은 2월달",end=" || ")
print("사과와 배, 딸기",end="  ")
print("월드컵 축구")
#지금은 2월달 || 사과와 배, 딸기
print()
#\\ : 리버스 슬래시를 뜻함
print("\\ \\ \\ \\")#\ \ \ \
print()
print("""동해물과
      백두산이
      마르고
      닳도록""")#""""""엔터키 치는 것만으로 \n친것처럼 출력됨
'''
동해물과
      백두산이
      마르고
      닳도록
'''
print()
print('''동해물과
      백두산이
      마르고
      닳도록''')
'''
동해물과
      백두산이
      마르고
      닳도록
'''
print("""
      동해물과
      백두산이
      마르고
      닳도록""")
'''
      동해물과
      백두산이
      마르고
      닳도록
'''
print(""" 
      동해물과
      백두산이
      마르고
      닳도록1234
      """,end="")# : 엔터 무시해라
print("""\
      동해물과
      백두산이
      마르고
      닳도록\
      """)
'''
      동해물과
      백두산이
      마르고
      닳도록1234
            동해물과
      백두산이
      마르고
      닳도록


'''
print(len("반갑다"))#3 : 길이가 3이다.
print("반갑다"[0])
print("반갑다"[1])
print("반갑다"[2])
'''
반
갑
다
'''
print()
print("반갑다"[0])
print("반갑다"[-1])
print("반갑다"[-2])
'''
반
다
갑
'''
print()

#-대문자, 소문자 바꾸기 : upper(), lower(), swapcase(), title()

print("eren is a hero."[0:4])#eren
print("eren is a hero."[10:14])#hero
print("eren is a hero."[-5:-1])#hero
#print("eren is a hero."[-5:0]) 섞어쓰면 안됨(error)
print()
print("stellaris"+" "+"nemesis");#stellaris nemesis
print("stellaris nemesis"[10:])#nemesis
print("stellaris nemesis"[:9])#stellaris
print("stellaris nemesis"[:])#stellaris nemesis
print("stellaris nemesis"[-17:-7])#stellaris
print("stellaris nemesis"[-7:])#nemesis

#문자열 반복연산자
print(3*"Hi")#HiHiHi

#indexError (index out of range) exception
#리스트/문자열/배열의 길이를 넘는 요소나 글자를 고를때 일어남
#IndexError: string index out of range <- 이런 글들로 나옴
print()
#산술연산자
'''
/ : 그냥 나눔
// : 나누고 소수점 아래는 없애고 정수파트만 나옴
'''

print("6/4 : ",6/4)#6/4 :  1.5
print("6//4 =", 6//4)#6//4 = 1
print("5%2 = ",5%2);#5%2 =  1
print("2**4 = ",2**4)#2**4 =  16
#곱셈, 나눗셈이 덧셈, 뺄셈보다 먼저 
#앞을 전제로 앞부터 먼저
#괄호 써서 바꿀수 있음
#수학이랑 똑같음

#복합 대입 연산자
'''
+= : 더한뒤 대입
=+ " 대입한 뒤에 더함
-,*,/,%,**도 다 똑같음


'''

a=5
#a=a+5
a+=5
print(a)#10
b=2
#b=b**4
b**=4
print(b)
name="Mikasa"
name+=" "
name+="Ackermann"
print("name : %s"% name)#name : Mikasa Ackermann


