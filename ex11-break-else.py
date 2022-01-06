def password(lista_passw):
    '''Três tentativas para introduzir corretamente uma password.'''
    conta = 3
    while conta:
        codigo = input("Entre o seu código sff:")
        if codigo in lista_passw:
            print("Bem-vindo(a)")
            break
        print("Código errado.")
        conta = conta - 1
    else:
        print("Acabaram suas tentativas!")
