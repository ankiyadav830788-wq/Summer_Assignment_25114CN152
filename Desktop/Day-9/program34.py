# Reverse Number Triangle

def rev(n) :
    
    for i in range(n,0,-1):
        for k in range(1,i+1):
            print(k,end="")
        print()
rev(5)