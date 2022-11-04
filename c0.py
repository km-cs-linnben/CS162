c0 = int(input("Enter a number "))
steps = 0
if c0 > 1:
    while c0 != 1:
        if c0%2 == 0:
            c0 /= 2
            print(c0)
            steps += 1
        else:
            c0 = (c0*3)+1
            print(c0)
            steps += 1
else:
    print("invalid number")
print("steps = ",steps)
