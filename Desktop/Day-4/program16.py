lower=int(input("enter a number"))
upper=int(input("enter a number"))
for num in range(lower,upper+1):
    temp=num
    count=0
    while temp>0:
        count+=1
        temp=temp//10
    temp=num 
    sum=0
    while temp>0:
         digit=temp%10
         sum=sum+digit**count
         temp=temp//10
    if num==sum:
        print(num)