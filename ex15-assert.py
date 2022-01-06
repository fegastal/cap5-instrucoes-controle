'''O resultado da chamada com n = 100 terá alerta:
AssertionError: Valores fora dos limites.'''


def exe_ass(n):
    assert 7 < n < 77, 'Valores fora dos limites'
    print (n)