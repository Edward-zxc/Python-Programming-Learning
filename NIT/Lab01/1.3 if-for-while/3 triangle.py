height = int(input("Height: "))

for i in range(1,height-1):
    for j in range(1,height-i-1):
        print(" ",end="")
    for k in range(1,i+1):
        print("#",end="")
    print(" ")
    for l in range(1,i+1):
        print("#",end="")
    print()