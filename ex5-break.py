def factor_max(y):
    x = y//2
    while x > 1:
        if y % x == 0:
            print(f"O maior fator de {y} é de {x}")
            break
        x = x-1

