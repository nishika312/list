a=[1,2,4,8,6,]
i=0
k=[]
while i<len(a):
    if a[i]%2==0:
        k.append(a[i])
    i=i+1
print(k)
