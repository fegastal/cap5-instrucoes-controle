import math

def quad_perfeito(n):

    for num in range(n, 0, -1):
        raiz = math.sqrt(num)
        if raiz == int(raiz):
            print(f"Maior quadrado perfeito menor do que {n} é de {num}")
        break
