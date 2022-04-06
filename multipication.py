
list=[6,1,3,5,6,3,1]
i=0
a=[]
product=1
while i<len(list):
    if list[i] not in a:
        a.append(list[i])
    i+=1
print(a)
i=0
while i<len(a):
    product=a[i]*product
    i+=1
print(product)


