def gdc(a, b):
    return a if b == 0 else gdc(b, a % b)


print(gdc(48, 42))
