# Half Pyramid

def pattern():
    num = int(input("Enter the size: "))

    for rows in range(1, num + 1):
        for cols in range(rows):
            print("*", end="")
        print()

pattern()