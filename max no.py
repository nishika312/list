num= [50, 40, 23, 70, 56, 12, 5, 10, 7]
b=0
i=0
while i<len(num):
    if num[i]>b:
        b=num[i]
    i=i+1
print(b)