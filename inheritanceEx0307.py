#inheritanceEx0307.py
class Person:
    
    #생성자메서드(constructor method)
    #– 클래스 이름과 똑같은 함수
    
    def __init__(self,*args, **kwargs):#Person클래스를 복사해서 메모리에 붙임
        #멤버변수들 초기화하기
        #클래스 내부의 멤버함수는 첫 번째 매개변수로 반드시 self 입력해야 함
        
        #자바나 c++은
        #this.필드 = 필드
        if len(args) == 0:
            self.name = None
            #self.name = "Donald Trump"
            self.age = 0
            self.blood = None
            print("I am a Person constructor method.")
        elif len(args) == 3:
            self.name = args[0]
            self.age = args[1]
            self.blood = args[2]
            print("I am a Person constructor method that has three arguements")
        elif len(args) == 2 and len(kwargs) == 1:
            self.name = args[0]
            self.age = args[1]
            self.blood=kwargs["blood"]#딕셔너리라서
            print("I am a Person that is kwargs_constructor method that has 3 arguements")
        #• self : ‘자기 자신’을 나타내는 딕셔너리, 주소를 참조함
        #• 멤버변수나 멤버메서드에 접근할 때 self.<식별자> 형태로 접근
    def setBlood(self,blood : str):
        self.blood = blood
    
    def getBlood(self):
        return self.blood
    
    def setName(self,name : str):
        self.name=name
    
    def getName(self):
        return self.name
    
    
    def setAge(self, age : int):
        self.age=age
    
    def getAge(self):
        return self.age
    
    
    def breathe(self):
        print("%s is breathing."%self.name)
        print("self.name=%s" %self.name)
        print()
    
    def speak(self):
        print("%s is speaking."%self.name)
        print("self.age=%d" % self.age)
        print()
    
    def showData(self):
        print("name = %s, age = %d, blood = %c" %(self.name,self.age,self.blood))
class Man(Person):#inheritance in python, 자식클래스이름(부모클래스이름)
    def showData2(self):
        super(Man,self).__init__()
        print("self.money = %d, self.job = %s" %(self.money,self.job))
    
    def __init__(self,*args,**kwargs):
        if len(args) == 0:
            #super(Man, self).__init__()#자식인 맨클래스에서 맨의 슈퍼클래스의 멤버에 접근하겠다.
            #없으면 있는 것으로 다루고 넘어감
            super(Man, self).__init__()
            self.money=0
            self.job=None
            print("I am primitive constructor of Man")
        elif len(args)==2:
            self.money=args[0]
            self.job=args[1]
        elif len(args)==5:
            super(Man, self).__init__(*(args[0],args[1],args[2]))#상속할 때 *가 붙어있는 매개변수를 넣음
            #self.name=args[0]
            #self.age=args[1]
            #self.blood=args[2] 겹쳐서 필요없음
            self.money=args[3]
            self.job=args[4]
            print("I am constructor that has 5 arguements.")
            

    def work(self):
        print("%s is working."%self.name)
        self.money=70000
        print("self.money = %d"%self.money)
        print("self.name = %s" %self.name)

'''부모클래스(슈퍼클래스)에 만들어진 필드, 메소드를 자식클래스(서브클래스)가
물려받음
 부모의 생물학적 특성을 물려받는 유전과 유사
▪ 상속을 통해 간결한 자식 클래스 작성
 동일한 특성(멤버변수와 멤버메소드)을 재정의할 필요가 없어 자식 클래스가
간결해짐'''
 
#메인코드  
if __name__ == "__main__":
    #I am a Person constructor method.
    person1 = Man()#I am primitive constructor of Man
    person1.setBlood("O")
    person1.setName("손흥민")
    person1.work()

'''
he is working.
self.money = 70000
self.name = 손흥민
'''
person1.setAge(37)
#person1.age = 37
person1.speak()#A person is speaking.
#self.age=37
person1.showData()#name = 손흥민, age = 37, blood = O
print("-------------------------")
person2=Man("joan",48,'A',80000,"celebrity")
#I am a Person constructor method.
#I am constructor that has 5 arguements.
person2.showData()#name = joan, age = 48, blood = A
person2.showData2()#self.money = 80000, self.job = celebrity


    