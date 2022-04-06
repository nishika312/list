a=[64, 25, 12, 22, 11, 1,2,44,3,122, 23, 34] 
i=0
while i<len(a):
    j=0
    while j<len(a):
        if a[i]<a[j]:
            m=a[i]
            a[i]=a[j]
            a[j]=m
        j=j+1
    i=i+1
print(a) 