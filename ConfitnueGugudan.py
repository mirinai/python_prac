for i in range(1,11,1):
    if i % 2 ==0:
        continue#continue : skip(무시하고 건너뛰어라)
        #print("haha")#실행 안됨
    print("i=",i)

'''
i= 1
i= 3
i= 5
i= 7
i= 9
'''


'''dan, val=2,1

for dan in range(2,10,1):
    for val in range(1,10,1):
        print("%d x %d = %d"%(dan,val,dan*val), end="\n")'''

#구구단 출력
#val=1
#dan=2
for val in range(1,10,1):
    if val==4:
        continue
    for dan in range(2,6,1):
        if dan== 4:
            continue
        print("%d x %d = %d"%(dan,val,dan*val), end="\t")
        if dan==5:
            print()#print(end="\n")와 같은 일함
        
print()
for val in range(1,10,1):

    for dan in range(6,10,1):
        if dan== 6:
            continue
        print("%d x %d = %d"%(dan,val,dan*val), end="\t")
        if dan==9:
            print()#print(end="\n")와 같은 일함

