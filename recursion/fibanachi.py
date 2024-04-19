def fib(x):
    if x >= 2:
        return fib(x - 1) + fib(x - 2)
    else:
        return x


def fib_din(n):
    if n >= len(fib_list):
        for i in range(len(fib_list), n + 1):
            fib_list.append(fib_din(i - 1) + fib_din(i - 2))
    return fib_list[n]


fib_list = [0, 1]

print(fib_din(20577))  # максимльное значение
