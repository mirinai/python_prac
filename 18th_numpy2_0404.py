import numpy as np
list1=[[1,11],[2,12],[3,13]]
print("list1 :")
print(list1)
'''
list1 :
[[1, 11], [2, 12], [3, 13]]
'''
print()
print("list1[2] :")
print(list1[2])
'''
list1[2] :
[3, 13]
'''
print()
print("list1[:][1] :",list1[:][1])#list1[:][1] : [2, 12]
print()
list2=np.array(list1)

print("list2[ :,1] :")#모든
print(list2[ :,1])
'''
list2[ :,1] :
[11 12 13]
'''

print()


