num1=int(input("enter first number"))
num2=int(input("enter second number"))
greater=max(num1,num2)
while True:
    if greater%num1==0 and greater%num2==0:
        lcm=greater
        break
    greater+=1
print("LCM=",lcm)