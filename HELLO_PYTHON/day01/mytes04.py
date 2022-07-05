firstNum = int(input('첫수를 입력하시오 >> '))
lastNum = int(input('끝수를 입력하시오 >> '))
arr = range(firstNum,lastNum+1)

sum = 0
#for i in range(firstNum,secondNum+1) 이것도 가능함...
for i in arr:
    sum+=i
print(str(firstNum)+"부터",str(lastNum)+"까지의 합은",str(sum)+"입니다.")