n=int(input("enter a number"))
a=0
b=1
print("fibonacci serires")
print(a)
for i in range(0,n-1):
    c=a+b
    a=b
    b=c
    print(a)
