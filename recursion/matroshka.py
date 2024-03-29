def matroshka(x):
    if x < 2:
        print(f'Верх - {x}')
        print(f'Низ - {x}')
    else:
        print(f'Верх - {x}')
        print('---')
        matroshka(x-1)
        print('---')
        print(f'Низ - {x}')


matroshka(4)
