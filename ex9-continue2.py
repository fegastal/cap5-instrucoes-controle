def codigo():
    '''Pedir um código com exatamente quatro caracteres.'''
    while True:
        cod = input("Código sff:")
        if len(cod) != 4:
            print("O código tem de ter 4 caracteres.")
            continue
        else:
            print("Bem-vindo(a)!")
            break
