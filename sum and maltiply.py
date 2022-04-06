# do sum half sum and maltipletion

a=[1,2,3,4,5,6,7,8,9,10]
i=0
sum=0
k=1
while i<len(a):
    if i<5:
     sum=sum+(a[i])
    else:
        k=k*(a[i]) 
    i=i+1
print(sum)
print(k)
