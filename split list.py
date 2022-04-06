num=["i","s","h","u"]
i=0
sum=""
while i<len(num):
    j=0
    while j<len(num[i]):
        sum=sum+num[i][j]
        j+=1
    i+=1
print(sum)







