n= [50, 40, 23, 70, 56, 12, 5, 10, 7]
i=0
b=0
while i<len(n):
    if n[i]>=b:
        b=n[i]
    i=i+2
print(b)