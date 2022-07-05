from random import random

idx = int(random()*10)
print(idx)
com = ""
if idx%2 == 0:
    com="짝"
else:
    com="홀"
me = input("홀짝을 입력하시오 >> ")
print("나",me)
print("컴퓨터",com)
if me==com:
    print("결과 이김")
else:
    print("결과 짐")

