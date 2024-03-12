from math import sin,cos,tan,floor,ceil#모듈에서 어떤 함수만 가져오고 싶을 때
#import math
import numpy as np
import matplotlib.pyplot as plt

print("math.sin(1) :", sin(1))#math.sin(1) : 0.8414709848078965
print("math.cos(1)=", cos(1))#math.cos(1)= 0.5403023058681398
print("math.ceil(2.1)=", ceil(2.1))#math.ceil(2.1)= 3
#소수점 올리기
x = np.arange(1,10)
y = x*5
plt.plot(x,y)
plt.savefig('plot.png')

