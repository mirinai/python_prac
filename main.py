#test_package패키지 안 모듈을 모두 읽어들임
from test_package import *
print("module_a:",module_a.variable_a)#module_a: a 모듈의 변수
print("module_b:",module_b.variable_b)#module_b: b 모듈의 변수
print()
import test_package.module_a as a
import test_package.module_b as b
print("a.variable_a=",a.variable_a)#a.variable_a= a 모듈의 변수
print("b.variable_b=",b.variable_b)#b.variable_b= b 모듈의 변수
print()
from test_package import module_a, module_b
#from test_package import module_b
print("모듈의 진짜 이름을 쓰기")
print(module_a.variable_a)
print(module_b.variable_b)
'''
모듈의 진짜 이름을 쓰기
a 모듈의 변수
b 모듈의 변수
'''


