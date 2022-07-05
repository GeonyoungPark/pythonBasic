a = int(input("출력할 구구단을 입력하시오"))

for i in range(1,9+1):
    # print(a,"X",i,"=",a*i)
    print("{} X {} = {}".format(a,i,a*i))