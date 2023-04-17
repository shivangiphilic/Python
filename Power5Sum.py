def series(n):
    if n == 1:
        return 1
    else:
        return n**5 + series(n-1)


n = int(input("Enter a natural number: "))
print("Sum of series is",series(n))