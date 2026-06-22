# Repeated Characters Pattern 

def rep():
    
    ch = 'A'
    for i in range(1,6):
        for k in range(i):
            print(ch,end=" ")
        print()
        ch = chr(ord(ch)+1)   
rep()