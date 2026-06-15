n=int(input("enter a number"))
number=n
reverse=0
while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n=n//10
print(reverse)
if reverse==number:
    print("n is a pallindrome")
else :
    print("n is not a pallindrome")
    
