arr = range(100,200+1)
# print(list(arr))
sum = 0
for i in arr:
    if i%2 == 0:
        sum+=i
print("sum >> ",sum)