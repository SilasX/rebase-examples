def sumof2(x, y):
    return x + y

def fac_recursive(n):
    "This is better because it makes use of tail-call magic juice."
    if n == 0:
        return 1
    return n * fib_recursive(n - 1)

def fac_iterative(n):
    "Don't bother"
    out = 1
    for x in xrange(1, n + 1):
        out *= x
    return out


if __name__ == "__main__":
    print "Hello World!"
