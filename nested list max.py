
# nested list of max value
# "o/p[10]"
a=[[1,2,3,4],[4,5,8,1]]
i=0
sum=0
k=[]
while i<len(a):
    j=0
    while j<len(a[i]):
        sum=sum+(a[i][j])
        j=j+1
    k.append(sum)
    i=i+1
print(max(k))  

