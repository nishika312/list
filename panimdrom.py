a=["m","o","m"] # find palindrom number
b=a
i=-1
sum=""
while i>=-len(a):
    sum=sum+a[i]
    i-=1
if list(sum)==b:
    print("palindrom")
else:
    print("not palindrom")
    
    