myList=[1,2,3,4,5]
def add10(num):
    return num+10

for i in range(len(myList)):
    myList[i] = add10(myList[i])


print("myList=", myList)#myList= [11, 12, 13, 14, 15]

myList2=[1,2,3,4,5]
add10Two = lambda num : num+10
myList2=list(map(add10Two,myList2))# 11,12,13,14,15


print("myList2=", myList2)#myList2= [11, 12, 13, 14, 15]