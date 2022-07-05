import time
class Cat:
    def __init__(self):
        print("constructor")
    def __del__(self):
        print("destroyer")
    def crying(self):
        print("meow")
    def __str__(self):
        return "babo"

c = Cat()

c.crying()
time.sleep(4)
print(c)