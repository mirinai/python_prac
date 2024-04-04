import numpy as np

x = np.array([1,3,5])
print("x :")
print(x)#[1 3 5]
print("x.mean(x) :")
print(x.mean())#3.0

print()
print("x.shape :",x.shape)#x.shape : (3,)
print()
y=np.array([1,3,5,7,9,11])
print("y.shape :",y.shape)#y.shape : (6,)
print()
print('y :')
print(y)#[ 1  3  5  7  9 11]

print()
y2=y.reshape(3,2)
print('y2.shape :',y2.shape)#y2.shape : (3, 2)
print(y2)
'''
[[ 1  3]
 [ 5  7]
 [ 9 11]]
'''
print()
x2 = np.array([ [1,3,5],[2,4,6]])
print("x2 :")
print(x2)
'''
x2 :
[[1 3 5]
 [2 4 6]]
'''
print("x2[0] :")
print(x2[0])
'''
x2[0] :
[1 3 5]
'''
print()
print("x2[1] :")
print(x2[1])
'''
x2[1] :
[2 4 6]
'''
print()
print("x2.mean() :",x2.mean())#x2.mean() : 3.5

print()
print("x2[1].mean() :",x2[1].mean())#x2[1].mean() : 4.0

