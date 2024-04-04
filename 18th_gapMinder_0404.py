import numpy as np
import pandas as pd

#같은 폴더에 gapminder.tsv가 있다는 가정으로 하기
df = pd.read_csv("./18thPandasNumpyEx0404/gapminder.tsv",sep="\t")
#df = pd.read_csv("gapminder.tsv",sep='\t')
print("df :")
print(df)
print("head() 함수를 써서 앞부분 다섯 줄만 출력하기")
print(df.head())
'''
       country continent  year  lifeExp       pop   gdpPercap
0  Afghanistan      Asia  1952   28.801   8425333  779.445314
1  Afghanistan      Asia  1957   30.332   9240934  820.853030
2  Afghanistan      Asia  1962   31.997  10267083  853.100710
3  Afghanistan      Asia  1967   34.020  11537966  836.197138
4  Afghanistan      Asia  1972   36.088  13079460  739.981106
'''
print()
print(df.head(3))
'''
       country continent  year  lifeExp       pop   gdpPercap
0  Afghanistan      Asia  1952   28.801   8425333  779.445314
1  Afghanistan      Asia  1957   30.332   9240934  820.853030
2  Afghanistan      Asia  1962   31.997  10267083  853.100710
'''
print()
print("df의 데이터타입 =",type(df))
#df의 데이터타입 = <class 'pandas.core.frame.DataFrame'>


print("df의 차원을 구해주는 shape 속성")
print("df.shape=",df.shape)#df.shape= (1704, 6)
#axis=0 : 1704, axis=1 : 6
print()
print("df.shape[0]=",df.shape[0])
print("df.shape[1]=",df.shape[1])
'''
df.shape[0]= 1704
df.shape[1]= 6
'''
