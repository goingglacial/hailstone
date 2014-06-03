# Hailstone code below.
def buggle(n):
    count = 0
    while n != 1:
        print n,
        if n % 2 == 0:
            n = n / 2
        else:
            n = (n*3) + 1
        count = count + 1
    print n
    print "It took" , count , "steps to get to 1."

buggle(36)