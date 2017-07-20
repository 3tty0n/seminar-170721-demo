import time

def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)

def entry_point(argv):
    """
    entry point into the RPython
    it should return integer value
    """
    start = time.time()
    for i in xrange(1, 30):
        print fib(i)
    elapsed_time = time.time() - start
    print "elapsed_time:", elapsed_time

    return 0


def target(*args):
    """
    specific function that defines `entry_point`
    """
    return entry_point, None

if __name__ == "__main__":
    """
    this block is not executed in RPython
    because of CPython compatibility
    """
    import sys
    entry_point(sys.argv)
