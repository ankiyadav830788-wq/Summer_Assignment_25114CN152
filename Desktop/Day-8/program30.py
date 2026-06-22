# Number Triangle 

def triangle(size) :
    
    for i in range(1,size+1):
        for k in range(1,i+1):
            print(k,end="")
        print()
triangle(5)