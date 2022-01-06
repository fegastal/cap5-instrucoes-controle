def try_1(x):
    try:
        y = eval(input("\nDenominador: "))
        print(x / y)
    except ZeroDivisionError:
        print("\nCuidado: o denominador não pode ser zero!")
