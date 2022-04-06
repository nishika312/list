# n="ishu" # devid element with string
# a=list(n)
# print(a)(

# a=[1,[2,3[4,5]],[6,7,8]],[10],[11]
# a=[2,3,4,],[5,6,7,8,],[45,6,7,8,9]
# print(a[0][2])
# print(a[1][3])
# print(a[2][4])

# a=[1,2,3,4,6,7]
# print(a[2])
# print(a[3])


# a=[1,2,4,2,5,2,1,2] # do not want repeted value
# i=0
# k=[]
# while i<len(a):
#     if a[i] not in k:
#         k.append(a[i])
#     else:
#         pass    
#     i+=1
# print(k)

# from stringprep import in_table_b1


# name=["apple","banana","bubble","gruff"] # iterate the list and element
# animal=["cat","dog","fish","goat"]
# age=[5,6,7,8]
# i=0
# while i<len(name):
#     print(name[i],"the",animal[i],"is",age[i])
#     i=i+1
   

# list sum:-

# a=[1,2,3,4]
# i=0
# sum=0
# k=[]
# while i<len(a):
#     sum=sum+(a[i])
#     k.append(sum)
#     i=i+1
# print(k)

# nested list of sum
# "o/p[10]"
# a=[[1,2,3,4],[4,3,2,1]]
# i=0
# sum=0
# k=[]
# while i<len(a):
#     j=0
#     while j<len(a):
#         sum=sum+(a[i][j])
#         k.append(a)
#         j=j+1
#     i=i+1 
# print(sum)   


# from re import I


# a=[1,2,4,8,6,]
# i=0
# k=[]
# while i<len(a):
#     if a[i]%2==0:
#         k.append(a[i])
#         # print(k)
#     i=i+1
# print(k)




               # arange the list numbers
# a=[1,2,3,2,6,5,7,9,4,1]   
# i=0 

# number=[1,5,6,9,0]
# for i in range(len(number)):
#     for j in range(i+1,len(number)):
#         if number[i]<number[j]:
#          number[i],number[j]=number[j],number[i]
# print(number)




#arange the list:-

# a=[64, 25, 12, 22, 11, 1,2,44,3,122, 23, 34] 
# i=0
# while i<len(a):
#     j=0
#     while j<len(a):
#         if a[i]<a[j]:
#             m=a[i]
#             a[i]=a[j]
#             a[j]=m
#         j=j+1
#     i=i+1
# print(a)            
 
# a=[1,2,3,4,5,6,7,8,9,10]
# i=0
# sum=0
# k=1
# while i<len(a):
#     if i<5:
#      sum=sum+(a[i])
#     else:
#         k=k*(a[i]) 
#     i=i+1
# print(sum)
# print(k)

 
# # o/p=["h",5,"u",10,"s","15","n","20","a","25"]

# a="ishu"
# i=0
# k=[]
# c=5
# while i<len(a):
#     k.append(a[i])
#     k.append(c)
#     c=c+5
#     i=i+1
# print(k)

# a="my name is ishu"
# i=0
# coun=0
# b=[]
# while i<len(a):
#     if a[i]==" ":
#         coun=coun+1
#     i=i+1
# print(coun)

# a=[64, 25, 12, 22, 11, 1,2,44,3,122, 23, 34]
# i=0
# while i<len(a):
#     a.sort()
#     i=i+1
# print(a)



# a=[64, 25, 12, 22, 11, 1,2,44,3,122, 23, 34]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a):
#         if (a[i])<(a[j]):
#             c=(a[i])
#             (a[i])=(a[j])
#             (a[i])=c
#             j=j+1
#         i=i+1
# print(a)

# from traceback import print_tb

# a="pinky loves ram so much"
# i=0
# count=0
# while i<len(a):
#     count=count
#     i=i+1
# print(count)
    
# a=[1,2,3,4,5,6,]
# i=0
# while i<len(a):
#     if i%2==0:
#         print(i,"even no")
#     else:
#         print(i,"ode no")
#     i=i+1
            
# a=[-1,3,[3,5],0,-1,7]
# i=0
# b=0
# while i<len(a):
#     j=0
#     while j<len(a):
#        if i>j:
#           b=(a[j])
#           (a[i])=(a[j])
#        j=j+1
#     i=i+1
# print(b,"min")

# a=[1,4,2,3,5,11,18,4,6,12,9]
# i=0
# k=[]
# while i<len(a):
#     j=1
#     count=0
#     while j<=(a[i]):
#         if (a[i])%j==0:
#             count+=1
#         j=j+1
#     if count==2:
#         k.append(a[i])
#     i=i+1
# print(k,"prime")


# from re import I


# a=[1,2,3]
# b=[4,5,6]
# c=[7,8,9]
# i=0
# n=[]
# while i<len(a):
#     j=0
#     while j<len(b):
#         b=0
#         while b<len(a):
#             k=(a[i])
#             (a[i])=(b[j])=(c[k])
#             n.append(k)
#             b=b+1
#         j=j+1
#     i=i+1
# print(k)    

a=[1,2,3]
b=[4,5,6]
c=[7,8,9]
# i=0
k=[]
# while i<len(a):
#     m=[a]=[b]=[c]
#     k.append(m)
#     i=i+1
# print(m)
    
k.append(a)
k.append(b)
k.append(c)
print(k)


a=[1,2,3]
i=0
while i<len(a):
    
