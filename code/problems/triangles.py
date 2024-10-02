

n = int(input("Enter size of triangle: "))

for i in range(n):
    for j in range(i + 1):
        print("*", end=" ")
    print()

print("------------")

for i in range(n, 0, -1):
    for i in range(i):
        print("*", end=" ")
    print()

for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(i + 1):
        print("*", end=" ")
    print()

print("------------")

for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()
