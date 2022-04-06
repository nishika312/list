m=["g","f","g"],["i","s"],["b","e","s","t"] # remove all string in the list
i=0
sum=0
a=[]
while i<len(m):
    j=0
    while j<len(m[i]):
        b=m[i][j]
        a.append(b)
        c="".join(a)
        j=j+1
    i=i+1
print(c)



