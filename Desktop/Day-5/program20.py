n=int(input("enter a number"))
for num in range(n,1,-1):
    count=0
    for i in range(1,num+1):
        if num%i==0:
         count+=1
    if count==2:
       print("largest prime number is",num)
       break
