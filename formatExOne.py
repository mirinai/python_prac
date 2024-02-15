format_a = "{}만원".format(7000)
print("format_a=" , format_a)#format_a= 7000만원
print("format_a=%s" % format_a)#format_a=7000만원

f_b = \
"열공해서 연봉{}만원 달성".format(6000)#\ : 엔터 무시함, {}안에 "6000"의 문자열 넣기
'''f_b = "열공해서 연봉{}만원 달성".format(6000) 와 같음'''
f_c="{}{}{}".format(30,40,50)
f_d="{}{}{}".format(3,"cat", True)#다 문자열로 만들어서 붙여버림
print("f_b=%s"  %  f_b)#f_b=열공해서 연봉6000만원 달성
print("f_c=" , f_c)#f_c= 304050
print("f_d=%s" % f_d)#f_d=3catTrue

#정수 출력
a = "{:d}".format(52)
print("a=" , a)#a= 52
print("a=%s" % a)#a=52
print("True - > 정수로 출력 -> {:d}".format(True))#True - > 정수로 출력 -> 1
print("False - > 정수로 출력 -> {:d}".format(False))#False - > 정수로 출력 -> 0
# 특정 칸에 출력하기
b = "{:5d}".format(52)
print("b=%s" % b)#b=   52
c = "{:10d}".format(52)
print("c=", c)#c=         52
#공백이 여덟개
#공백이 여덟개
#특정칸에맞춰서숫자를
#출력하는형태
c = "{:010d}".format(52)
print("c=", c)#c= 0000000052
#빈칸을 0으로 채우기
d = "{:05d}".format(52)
e = "{:05d}".format(-52)
print("d=" , d)#d= 00052, 
print("e=%s" % e)#e=-0052
