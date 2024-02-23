a = range(5)
print("a =",a)#a = range(0, 5)
print()
print("list(a) =",list(a))#list(a) = [0, 1, 2, 3, 4]
list_k=list(a)
print()
print("list_k =",list_k)#list_k = [0, 1, 2, 3, 4]

for n in range(4,-1,-1):
    print("지금 되풀이 변수: {}".format(n))
    '''
    지금 되풀이 변수: 4
    지금 되풀이 변수: 3
    지금 되풀이 변수: 2
    지금 되풀이 변수: 1
    지금 되풀이 변수: 0
    '''
print("\nreversed()함수를 쓴 거꾸로 되풀이 되는 반복문\n")
for n in reversed(range(5)):#==range(4,-1,-1)
    print("지금 되풀이 변수: {}".format(n))
    '''
    지금 되풀이 변수: 4
    지금 되풀이 변수: 3
    지금 되풀이 변수: 2
    지금 되풀이 변수: 1
    지금 되풀이 변수: 0
    '''
print("\n-------------\n")
#List Comprehensive(리스트 안에 포함)
myList = [ i*i for i in range(0,11,2)]

print("myList =",myList)#myList = [0, 4, 16, 36, 64, 100] : 0x0, 2x2, 4x4, 6x6, 8x8, 10x10
print("\n-------------\n")

