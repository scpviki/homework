n=int(input("enter a number"))
if n==0:
    count=1
else:
    count=0
    while n>0:
       count += 1
       n//=10
print(count)

