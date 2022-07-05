class Xi:
    def __init__(self):
        self.money = 1000
    def steal(self,smoney):
        self.money += smoney

class Putin:
    def __init__(self):
        self.nuclear = 5000
    def alzheimer(self):
        self.nuclear -= 1

class JungEun:
    def __init__(self):
        self.missile = 10000
    def ssorau(self):
        self.missile -= 100
        
class SungWoo(Xi,Putin,JungEun):
    def __init__(self):
        Xi.__init__(self)
        Putin.__init__(self)
        JungEun.__init__(self)  
        
class OOPTest:
    sw = SungWoo()
    sw.steal(500)
    sw.alzheimer()
    sw.ssorau()
    print(sw.money)
    print(sw.nuclear)
    print(sw.missile)
        
        
            
    