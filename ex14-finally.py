def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("divisão por zero!")
    else:
        print("o resultado é", result)
    finally:
        print("a executar a cláusula finally")
