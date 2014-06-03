# Hailstone code below.
def hailstone(n):
    count = 0
    print n, "is the starting number."
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = (n*3) + 1
        count = count + 1
        print n
    print "It took" , count , "steps to get to 1."

hailstone(36)
hailstone (37)
hailstone (39)