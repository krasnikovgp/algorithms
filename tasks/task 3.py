def f(n):
    if n > 2:
        return f(n-1) - f(n-2) + 2 * n
    return n


print(f(6))
