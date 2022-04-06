a=[1,2,3],[1,3,5],[7,3,6,8]
i=0
k=[]
while i<len(a):
    j=0
    while j<len(a[i]):
        if a[i]!=0:
            k.append(a[i][j])
        j=j+1
    i=i+1
print(k)
    
