import pandas as pd
s = pd.Series(["banana",42])
print(s)
'''
0    banana
1        42
dtype: object
'''
print()
s2 = pd.Series(['Wes McKinney', 'Creator of Pandas'])
print(s2)
'''
0         Wes McKinney
1    Creator of Pandas
dtype: object
'''
print()
s3 = pd.Series(['Wes McKinney', 'Creator of Pandas'],index=["the one","title"])
print(s3)
'''
the one         Wes McKinney
title      Creator of Pandas
dtype: object
'''
print("\n--------------\n")
x=pd.Series([7,3,5,8],index=["서울",'미추홀','매홀','곰나루'])
print(x)
'''
서울     7
미추홀    3
매홀     5
곰나루    8
dtype: int64
'''
print()
print("x=",x)
print("x['서울']=",x["서울"])
'''
x= 서울     7
미추홀    3
매홀     5
곰나루    8
dtype: int64
x['서울']= 7
'''
print("x['서울'] : "+str(x['서울'])+"| "+"x['미추홀'] : "+str(x['미추홀']))
#x['서울'] : 7| x['미추홀'] : 3
print()
print("x시리즈의 index : ",x.index)
print("x시리즈의 values : ",x.values)
#x시리즈의 index :  Index(['서울', '미추홀', '매홀', '곰나루'], dtype='object')
#x시리즈의 values :  [7 3 5 8]
#dtype: int64
#뜻 : 64bit
