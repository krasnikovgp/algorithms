def f(x: int, y: int) -> int:
    if x == y:
        return 1
    elif x > y or x == 17:
        return 0
    else:
        return f(x + 1, y) + f(x + 2, y) + f(x * 3, y)


print(f(3, 10) * f(10, 25))
