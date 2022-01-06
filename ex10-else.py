def primo(y):
    x = y//2
    while x > 1:
        if y % x == 0:
            print(f"{y} tem fator {x}")
            break
        x = x - 1
    else:
        print(f"{y}é um número primo.")
