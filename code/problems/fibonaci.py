"""
Fibonaci Sequence
"""


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def memoization_fib(n):
    if n <= 1:
        return n
    if n in mem:
        return mem[n]
    else:
        mem[n] = memoization_fib(n-1) + memoization_fib(n-2)
        return mem[n]


def bottom_up_fib(n):
    if n <= 1:
        return n
    a = 0
    b = 1
    for i in range(2, n+1):
        c = a + b
        a = b
        b = c
    return b


if __name__ == "__main__":
    n = int(input("Enter number: "))
    mem = {}
    # print(fib(n))
    # print(memoization_fib(n))
    print(bottom_up_fib(n))
