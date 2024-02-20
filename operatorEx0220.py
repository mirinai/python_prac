p=5 
m=9
print("p<=m : ",p<=m)#p<=m :  True

print("p>m : ",p>m)#p>m :  False
print("\n--------------")
print("가방"=="하마")#False
print("가방"!="하마")#True 가와 하의 유니코드를 견줌 만약 첫 글자도 같으면 두번째 글자 견줌
print("가방"<"하마")#True
print("가방">"하마")#False

print("가방>하마 :","가방">"하마")#가방>하마 : False
print("가방<하마 : ","가방"<"하마")#가방<하마 : True

print()
#not : 참 ->거짓, 거짓 -> 참
#and : 모두 참이면 참 아니면 거짓
#or : 하나만 참이면 참 아니면 거짓
print("not(가방>하마) :",not("가방">"하마"))#가방<하마 : True

print("not(가방<하마) :",not("가방"<"하마"))#not(가방<하마) : False

print("(4<5) and (8<9) :", (4<5) and (8<9))#(4<5) and (8<9) : True
print("(4<5) and (8>9) :", (4<5) and (8>9))#(4<5) and (8>9) : False
print("(4>5) and (8<9) :", (4>5) and (8<9))#(4>5) and (8<9) : False
print()
print("(4<5) or (8<9) :", (4<5) or (8<9))#(4<5) or (8<9) : True
print("(4<5) or (8>9) :", (4<5) or (8>9))#(4<5) or (8>9) : True
print("(4>5) or (8<9) :", (4>5) or (8<9))#(4>5) or (8<9) : True
print()

print("\n--------------")



