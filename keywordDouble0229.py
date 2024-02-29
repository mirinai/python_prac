def func(*args,**kwargs):#튜플, 딕셔너리
    print("위치기반 가변매개변수:",args)
    print("keyword기반 가변매개변수:",kwargs)
    for arg in args:
        print("arg=", arg)
    for key, value in kwargs.items():
        print(f"{key} : {value}")
        #print("{} : {}".format(key,value))

func(1,2,3,name="Jane",age=25)

'''
위치기반 매개변수: (1, 2, 3)
keyword기반 매개변수: {'name': 'Jane', 'age': 25}
arg= 1
arg= 2
arg= 3
name : Jane
age : 25
'''





