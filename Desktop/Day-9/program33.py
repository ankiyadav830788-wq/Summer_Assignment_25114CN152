# Star Reverse Pattern

def rev(size) :
    
    for i in range(size,0,-1):
        for k in range(i):
            print("*",end=" ")
        print()
rev(5)