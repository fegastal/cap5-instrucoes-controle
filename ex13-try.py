import math

def try_2():
    '''Cálculo das raizes reais de um polinômio.'''
    try:
        a,b,c = eval(input("Os coeficientes sff (a, b, c):\t"))
        discriminante = pow(b,2) - 4 * a * c
        raiz_discrim = math.sqrt(discriminante)
        raiz1 = (-b + raiz_discrim) / (2 * a)
        raiz2 = (-b - raiz_discrim) / (2 * a)
        if raiz1 == raiz2:
            print("O polinômio de coeficientes a=%d, b=%d, c=%d tem raízes múltiplas raiz1= raiz2=%3.2f"
                  % (a, b, c, raiz1, raiz2))
        else:
            print("As raízes do polinômio de coeficientes a=%d, b=%d, c=%d são raiz1=%3.2f raiz2=%3.2f"
                  % (a, b, c, raiz1, raiz2))
    except ValueError:
        print("\nNão tem raízes reais!")
