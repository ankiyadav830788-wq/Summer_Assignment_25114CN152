# Repeating Number Triangle

def triangle(size):

    for i in range(1, size+1):
        for k in range(i):
            print(i, end="")

        print()

triangle(5)