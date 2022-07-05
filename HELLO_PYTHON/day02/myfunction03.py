from random import random

def getHollJJak():
    if random() > 0.5:
        return "홀"
    else:
        return "짝"

com = getHollJJak()
print("com >>",com)