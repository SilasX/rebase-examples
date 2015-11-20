def sumof2(x, y):
    return sum(x, y)

def fac_recursive(n):
    """You should use this one because it's more elegant."
    """
    if n == 0:
        return 1
    return n * fib_recursive(n - 1)

def fac_iterative(n):
    """You shouldn't use this one because it's less elegant."
    """
    out = 1
    for x in xrange(1, n + 1):
        out *= x
    return out

def zip_iterative(f, list1, list2):
    listout = []
    for i, x in enumerate(list1):
        if i < len(list2):
            listout.append(f(x, list2[i]))

if __name__ == "__main__":
    print "Hello World!"
