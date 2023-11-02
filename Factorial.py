def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

n = 5
result = factorial_recursive(n)
print(f"{n}! = {result}")