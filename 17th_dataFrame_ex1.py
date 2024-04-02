import pandas as pd
'''
데이터프레임(DataFrame)
- 2차원 배열
- 행과 열로 구성
- 열(Column)에
대한 각각의
이름을 부여

'''
data ={"age":[23,43,12,45],"name":["john",'george','james','cyncia'],\
    'height':[175.3,180.3,165.8,172.7]}
#아직 딕셔너리
print("data :")
print(data)
print()
print(pd.DataFrame(data))
'''
   age    name  height
0   23    john   175.3
1   43  george   180.3
2   12   james   165.8
3   45  cyncia   172.7
'''
print()
x=pd.DataFrame(data,columns=['name','age','height'])

print("x :")
print(x)
'''
x :
     name  age  height
0    john   23   175.3
1  george   43   180.3
2   james   12   165.8
3  cyncia   45   172.7
'''
print("x의 타입 :")
print(type(x))
'''
x의 타입 :
<class 'pandas.core.frame.DataFrame'>
'''
print("----------")
arr=[[1,2],[3,4],[5,6]]
df = pd.DataFrame(arr,columns=["first","second"])
print("df :")
print(df)
'''
df :
   first  second
0      1       2
1      3       4
2      5       6
'''
print("----------")
#Pandas 에서 데이터를 행단위로 가져오기 위한 함수
print("df.iloc[1] : ")
print(df.iloc[1])
'''
df.iloc[1] :
first     3
second    4
Name: 1, dtype: int64
'''
print(df.iloc[2])
'''
first     5
second    6
Name: 2, dtype: int64
'''
print("df.iloc[:,-1] :")
print(df.iloc[:,-1])
'''
df.iloc[:,-1] :
0    2
1    4
2    6
'''
print("----------")
#head함수
arr2=[[1,2],[3,4],[5,6],[7,8],[9,10]]
df2= pd.DataFrame(arr2,columns=["one",'two'])
bools =[False,True,False,True,False]



print("df2 : ")
print(df2)
'''
df2 :
   one  two
0    1    2
1    3    4
2    5    6
3    7    8
4    9   10
'''
print("df2.head(3) :")
print(df2.head(3))
'''
df2.head(3) :
   one  two
0    1    2
1    3    4
2    5    6
'''
print("df2.head() :")
print(df2.head())
'''
df2.head() :
   one  two
0    1    2
1    3    4
2    5    6
3    7    8
4    9   10
'''
print("----------")
print("df2.tail() :")
print(df2.tail())
'''
df2.tail() :
   one  two
0    1    2
1    3    4
2    5    6
3    7    8
4    9   10
'''
print("df2.tail(3) :")
print(df2.tail(3))
'''
df2.tail(3) :
   one  two
2    5    6
3    7    8
4    9   10
'''
print("----------")
print("df2.two :")
print(df2.two)
'''
df2.two :
0     2
1     4
2     6
3     8
4    10
'''
print("df2.two[bools] :")
print(df2.two[bools])
'''
df2.two[bools] :
1    4
3    8
Name: two, dtype: int64
'''
print("----------")
data2 ={"age":[23,43,12,45],'height':[175.3,180.3,165.8,172.7]}
x2=pd.DataFrame(data,columns=['age','height'])
#아직 딕셔너리
print("data2 :")
print("x2 :")
print(x2)
'''
data2 :
x2 :
   age  height
0   23   175.3
1   43   180.3
2   12   165.8
3   45   172.7
'''
print()
print("x2의 타입 :",type(x2))
#x2의 타입 : <class 'pandas.core.frame.DataFrame'>
print()
print("x2.mean(axis=0) :")
print(x2.mean(axis=0))
'''
x2.mean(axis=0) :
age        30.750
height    173.525
dtype: float64
'''
print("------------------------------------------")
arr3=[[1,2],[3,4],[5,6],[7,8],[9,10]]
df3 = pd.DataFrame(arr3,columns=["수온","상온"])
print("df3 :")
print(df3)
'''
df3 :
   수온  상온
0   1   2
1   3   4
2   5   6
3   7   8
4   9  10
'''
print("수온을 실수로 바꾼 뒤 df3 출력 :")
df3['수온']=df3['수온'].astype("float")

print(df3)
'''
    수온  상온
0  1.0   2
1  3.0   4
2  5.0   6
3  7.0   8
4  9.0  10
'''
'''
Objects: 문자 또는
문자열형
- Int64: 정수형
- Float64: 실수형
Pandas 데이터의 형변환
- astype() 메소드 사용

'''



