"""
fACtorial OF A NUMBER
"""


def factorial(n: int) -> int:
    res = 1
    if n <= 1:
        return 1
    else:
        for i in range(1, n+1):
            res *= i
        return res


def factorial_recursive(n: int) -> int:
    if n <= 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


print("Factorial:", factorial(-4))
print("Factorial recursive:", factorial_recursive(-4))

print("Factorial:", factorial(5))
print("Factorial recursive:", factorial_recursive(5))
