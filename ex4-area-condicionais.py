import random
import math


def area_f(f, a, b, min_, max_, num_dardos):
    '''Calcula a área sob a curva f entre a e b.'''
    conta = 0
    area = (max_ - min_) * (b - a)
    for i in range(num_dardos):
        x = random.uniform(a, b)
        y = random.uniform(min_, max_)
        if y <= f(x):
            conta += 1
        percent = conta / num_dardos
        return percent * area


def f(x):
    return math.exp((-x ** 2)/2)


if __name__ == '__main__':
    print(area_f(f, 0, 2, 0, 1, 1000))