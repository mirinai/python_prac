import pandas as pd
'''
시리즈
- 복수의 행(row)으로 이루어진 하나의
열(column) 구조
- 색인(index)을 가지고 원하는 데이터에
접근할 수 있음
- 자동으로 색인을 만들어 줌
- 자동으로 색인을 만들지 않고 index 키워드를 사용해 원하는 색인의
이름을 입력
- 색인을 나열하여 원하는 값들을 출력

'''
x = pd.Series([7,3,5,8],index=['서울','대구','부산','광주'])

print(x)
'''
서울    7
대구    3
부산    5
광주    8
dtype: int64'''

print("오름차순 정렬된 x시리즈의 index : ",sorted(x.index))
#오름차순 정렬된 x시리즈의 index :  ['광주', '대구', '부산', '서울']
print("오름차순 정렬된 x시리즈의 values : ",sorted(x.values))
#오름차순 정렬된 x시리즈의 values :  [3, 5, 7, 8]

print("----------")
print("x.reindex(sorted(x.index)) : ")
print(x.reindex(sorted(x.index)))

'''
x.reindex(sorted(x.index)) :
광주    8
대구    3
부산    5
서울    7
dtype: int64
'''

y = pd.Series([2,4,5,1],index=['대구','부산','서울','대전'])

print("x+y : ")
print(x+y)
'''
x+y :
광주     NaN
대구     5.0
대전     NaN
부산     9.0
서울    12.0
dtype: float64
'''
#NaN : Not a Number
print("----------------------------")
medal=[1,3,2,4,2,3]
k = pd.Series(medal)
print("k : ")
print(k)
'''
k :
0    1
1    3
2    2
3    4
4    2
5    3
dtype: int64
'''
print("pd.unique(k) : ")
print(pd.unique(k))
'''
pd.unique(k) :
[1 3 2 4]
'''
print("----------------------------")
age = {'민준':23,'현우':43,"서연":13,"동형":45}
m = pd.Series(age)
print("m :")
print(m)
'''
m :
민준    23
현우    43
서연    13
동형    45
dtype: int64
'''
print("----------------------------")
a = medal[2:5]
print("a :")
print(a)
'''
a :
[2, 4, 2]
'''



