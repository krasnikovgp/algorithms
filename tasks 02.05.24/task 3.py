__import__("os").system("cls")


def f(x, y):
    if x == y:
        return 1
    if x > y:
        return 0
    else:
        return f(x + 2, y) + f(x + 4, y)
        print(x, y)
    

print(f(4, 22))
