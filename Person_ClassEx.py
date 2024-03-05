'''
객체지향프로그래밍:

처리하고자 하는 자료에 중점을 두고, 프로그램을 객체
(object)라는 것으로 모델화하는 프로그래밍

◼ 장점
◼ 소프트웨어의 확장성(extensibility) 향상
◼ 재사용(reusability)성 향상
◼ 프로그래머의 생산성(productivity) 증가
◼ 유지보수(maintainability) 비용 절감



실세계 객체의 특징
• 객체마다 고유한 특성(state)와 행동(behavior)를 가짐
• 다른 객체들과 정보를 주고 받는 등, 상호작용하면서 존재
▪ 컴퓨터 프로그램에서 객체 사례
• 테트리스 게임의 각 블록들
• 한글 프로그램의 메뉴나 버튼들

'''
'''클래스(class)
• 객체의 모양을 선언한 틀(캡슐화-Encapsulation)
• 객체의 공통된 특징 기술
• 객체의 특성과 행위 선언

▪ 객체(Object)
• 클래스의 모양대로 생성된 실체(instance)
• 메모리에서 물리적 공간을 갖는 구체적인 실체
• 클래스의 인스턴스(실체)
» 클래스를 구체화한 객체를 인스턴스(instance)라고 부름
» 객체와 인스턴스(instance)는 같은 뜻으로 사용

Object(객체) = Data(구성요소) + operation(행위)

Class(클래스) = field(변수 및 상수) + method(메서드)

'''
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
        print("A person is breathing.")
        print("self.name=%s" %self.name)
        print()
    
    def speak(self):
        print("A person is speaking.")
        print("self.age=%d" % self.age)
        print()
    # : 캡슐화 
'''
붕어빵 틀은 클래스이며, 이 틀의 형태로 구워진 붕어빵은 바로 객체입니다. 
붕어빵은 틀의 모양대로 만들어지지만 서로 조금씩 다릅니다. 
치즈붕어빵, 크림붕어빵, 앙코붕어빵 등이 있습니다. 
그래도 이들은 모두 붕어빵
객체(instance)입니다.

현실 세계의 붕어 객체(Object) -> Abstraction(Modeling) -> 복사시킴
-> 붕어빵 객체(instance)
''' 
#메인코드  
if __name__ == "__main__":

    trump = Person() #I am a Person constructor method.
    #()안에 self라는 매개변수가 들어있음,안보임
    
    #print("self.name = %s" %trump.name)#self.name = Donald Trump
    
    #trump.name = "Lara Croft" 캡슐화의 정보은닉에 안맞음
    
    trump.setName("Lara Croft")
    
    #print("trump.name = %s" %trump.name)#trump.name = Lara Croft ,캡슐화의 정보은닉에 안맞음
    
    print("trump.getName() = %s" %trump.getName())#trump.getName() = Lara Croft
    trump.setAge(28)
    

    
    print("trump.age = %d" % trump.getAge())#trump.age = 28
    print()
    
    trump.breathe()
    #A person is breathing.
    #self.name=Lara Croft
    trump.speak()
    #A person is speaking.
    #self.age=0
    print("\n-------------------")
    #wonbin = Person("원빈",39,blood='A')#"원빈",39 : *args에 튜플꼴로 넣어짐    blood='A' : **kwargs에 딕셔너리꼴로 넣어짐
    wonbin = Person("원빈",39,'A')
    print()
    print("wonbin.getName() = %s" %wonbin.getName())#wonbin.getName() = 원빈
    print()
    print("wonbin.age = %d" % wonbin.getAge())#wonbin.age = 39
    print()
    print("wonbin.blood = %c" % wonbin.getBlood())#wonbin.blood = A
