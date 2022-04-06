a=[[1,2,3],[5,4,3],[4,5,6,7],[4,5,6]] # do sum whith maltipal values of list
i=0
while i<len(a):
    j=0
    sum=0
    while j<len(a[i]):
        sum=sum+a[i][j]
        j=j+1
    i=i+1
    print(sum)



# b=a[2][1:2]
# print(b)