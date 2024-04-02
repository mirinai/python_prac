#tsv : Tap Seperated Value
import pandas as pd

df = pd.read_csv("17thPandasNumpyEx0402/gapminder.tsv",sep="\t")
#df = pd.read_csv("gapminder.tsv",sep="\t")

print("df :")
print(df)

print("-----------------------------------------------")
print("type(df)",type(df))
#type(df) <class 'pandas.core.frame.DataFrame'>
print("df데이터프레임의 차원 : df.shape :")
print(df.shape)#함수 아님, 속성
#(1704, 6) : 1704 rows, 6 columns
