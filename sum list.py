# a=[1,2,3,4,5,6,7,8,9,10]
# i=0
# sum=0
# while i<len(a):
#     sum=sum+a[i]
#     i+=1
# print(sum)





a=[1,2,3,[1,3,5],7,3,6,8]
i=0
sum=0
while i<len(a):
    if type (a[i])==list:
       j=0
       while j<len(a[i]):
           sum=sum+a[i][j]
           j=j+1
    else:
        sum=sum+a[i]
    i=i+1
print(sum)