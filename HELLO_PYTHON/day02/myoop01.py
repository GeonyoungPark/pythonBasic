class Animal:
    def __init__(self):
        self.age = 1
    def happyBirthday(self):
        self.age += 1
        
class Human(Animal):
    def __init__(self):
        super().__init__()
        self.money = 10000
    def albamon(self):
        self.money+=1
    
class OOPTest:
    
    gy = Human()
    print("나이 >>",str(gy.age)+"살")
    print("가진 돈 >>",str(gy.money)+"만원")
    gy.happyBirthday()
    gy.albamon()
    print("나이 먹은 후 >>",str(gy.age)+"살")
    print("알바한 후 >>",str(gy.money)+"만원")