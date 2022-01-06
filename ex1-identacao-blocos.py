x = 1
if x == 1:
    y = 2
    if y == 2:
        x = 2
        print('Bloco 2: x =%d, y =%d' % (x, y))
    y = 1
    print('Bloco 1: x=%d, y=%d' % (x, y))
x = 1
print('Bloco 0: x=%d, y=%d' % (x, y))
