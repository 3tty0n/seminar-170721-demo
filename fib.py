import time

def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def main():
    start = time.time()
    for i in xrange(1, 30):
        print fib(i)

    elapsed_time = time.time() - start
    print("elapsed_time:{0}".format(elapsed_time))


if __name__ == "__main__":
    main()
