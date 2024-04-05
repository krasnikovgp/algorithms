def gdc(a, b):
    if b == 0:
        return a
    else:
        return gdc(b, a % b)


print(gdc(48, 42))
