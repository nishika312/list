# from logging.handlers import RotatingFileHandler


a=[1,2,6,3,9,5]
# i=0
# k=[]
# while i<len(a):
#     fact=0
#     j=1
#     while j<=a[i]:
#         if a[i]%j==0:
#             fact+=1
#         j=j+1
#         # print("prime no")
#     # else:
#         # print("not prime")
#     i=i+1
#     if fact==2:
#         # print(a[i])
#         # print("prime number")
#         k.append(a[i])

#     # else:
#         # print("not prime number")
# print(k)


# print(a)
# l=len(a)
# for i in range(len(a)):
#     c=0
#     for j in range(2,a[i]):
#         if a[i]%j==0:
#             proint
#             c=c+1
#         # break
#     if c==2:
#         print(a[i],"is prime number")



a=[1,3,2,4,5,11,13,4,6,8,9]
i=0
l=[]
while i<len(a):
    j=1
    count=0
    while j<=a[i]:
        if a[i]%j==0:
            count+=1
        j=j+1
    if count==2:
        l.append(a[i])
    i=i+1
print(l)










        
