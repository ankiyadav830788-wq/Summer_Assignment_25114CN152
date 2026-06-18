n=int(input("enter a decimal number"))
binary=""
while n>0:
    rem=n%2
    binary=str(rem)+binary
    n=n//2
print("binary number=",binary)