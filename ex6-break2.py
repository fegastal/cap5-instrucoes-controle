def entradados():

    '''Exemplo de uso de break'''

    while True:
        nome = input("O seu nome:\t")
        if nome == 'stop':
            break
        idade = int(input("A sua idade:\t"))
        print(f"\nViva {nome}!\t {idade} é uma linda idade...")
