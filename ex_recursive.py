def bunny_ears(n):
    if n == 0:    #Base case
        return 0
    return bunny_ears(n-1)+2    #Recursive. Adds 2 every stack. Ends at 0 + 2 and works backwards from there

print(bunny_ears(5))    #Returns 10