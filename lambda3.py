a=[1,5,4,6,8,11,3,12]

#filter(lambda 변수 : 조건, 가져올 것)
even = list(filter(lambda x : (x%2)==0,a))#4,6,8,12
print("even=",even)#even= [4, 6, 8, 12]
ten_times = list(map(lambda x : x*10, a))
print("ten_times=",ten_times)#ten_times= [10, 50, 40, 60, 80, 110, 30, 120]
b=[[0,1,8],[7,2,2],[5,3,10],[1,4,5]]
b2=[[0,1,8],[7,2,2],[5,3,10],[1,4,5]]
b.sort(key = lambda x : x[2])#b리스트에서 정렬하는데 key에 x에 b안의 리스트가 들어가고 오른쪽에는 인덱스=2인 원소가 들어감
#리스트 마다의 [2]인 원소로 정렬시키기 
#==b.sort(key = lambda x : x[2], reverse=False)
b2.sort(key = lambda x : x[2],reverse=True)#오름차순 -> 내림차순
print("b리스트를 오름차순으로 나란히 놓은 결과 :", b)
#b리스트를 오름차순으로 나란히 놓은 결과 : [[7, 2, 2], [1, 4, 5], [0, 1, 8], [5, 3, 10]]
print("b2리스트를 오름차순으로 나란히 놓은 결과 :", b2)
#b2리스트를 오름차순으로 나란히 놓은 결과 : [[5, 3, 10], [0, 1, 8], [1, 4, 5], [7, 2, 2]]

print("----------------------")
num=[3,1,4,1,5,9,2,6]
sorted_num=sorted(num,reverse=True)#내림차순 => 리스트로 리턴
print("sorted_num :",sorted_num)#sorted_num : [9, 6, 5, 4, 3, 2, 1, 1]
print("정렬한 뒤의 처음의 리스트 num=",num)#정렬한 뒤의 처음의 리스트 num= [3, 1, 4, 1, 5, 9, 2, 6]
print("----------------------")
'''
sort() 메서드 : 리스트 자체를 정렬
    리스트 타입의 객체에만 쓸수 있으며
    원본리스트를 직접 바꿈
'''
numbers2=[3,1,4,1,5,9,2,6]
numbers2.sort(reverse=True)#내림차순으로 정렬
print("나란히 한 뒤의 원본 리스트 numbers2 :",numbers2)#나란히 한 뒤의 원본 리스트 numbers2 : [9, 6, 5, 4, 3, 2, 1, 1]