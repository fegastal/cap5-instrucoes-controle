import math


def main2():
    '''Cálculo das raízes reais de um polinómio.'''
    a, b, c = eval(input("Os coeficientes sff (a,b,c):\t"))
    r1, r2 = raizes1(a, b, c)
    if r1 == r2:
        print("Raízes múltiplas!!")
        print("As raízes do polinómio de coeficientes\
        a=%d b=%d c=%d são r1=%3.2f r2=%3.2f" % (a, b, c, r1, r2))


def raizes1(a, b, c):
    """Calcula as raizes reais."""
    discriminante = pow(b, 2) - 4 * a * c
    raiz_discrim = math.sqrt(discriminante)
    raiz1 = (-b + raiz_discrim) / (2 * a)
    raiz2 = (-b - raiz_discrim) / (2 * a)
    return raiz1, raiz2