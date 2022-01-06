def impares(x):
    '''Exemplo de uso de continue.'''
    while x:
        x = x - 1
        if x % 2 == 0:
            continue
        print("{x} é ímpar.")
    print("\nFinito!")
    return 0
