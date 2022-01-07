'''Exercícios Teóricos | Capítulo 5

1) O que entende por bloco e como é que este se relaciona com a indentação do código?

Indentar é o recuo do texto em relação a sua margem, ou seja, se antes de escrevermos uma instrução,
utilizamos 4 espaçamentos da margem esquerda até a instrução propriamente dita, podemos dizer que a
indentação utilizada possui 4 espaços.

Indentar é o recuo do texto em relação a sua margem, ou seja, se antes de escrevermos uma instrução,
utilizamo 4 espaçamentos da margem esquerda até a instrução propriamente dita, podemos dizer que a indentação
utilizada possui 4 espaços.

Em Python, a indentação possui função bastante especial, até porque, os blocos de instrução são
delimitados pela profundidade da indentação, isto é, os códigos que estiverem rente a margem esquerda,
farão parte do primeiro nível hierárquico. Já, os códigos que estiverem a 4 espaços da margem esquerda,
estarão no segundo nível hierárquico e aqueles que estiverem a 8 espaços, estarão no terceiro nível
e assim por diante.

Todos os blocos são delimitados pela profundidade da indentação e por isso, a sua importância,
é vital para um programa em Python. O mau uso, isto é, utilizar 4 espaçamentos enquanto deveríamos
estar utilizando 8, acarretará na não execução, ou então, no mal funcionamento em geral.

Blocos são uma ou mais instruções que devem ser executadas uma após a outra, de cima para baixo
da esquerda para a direita. Existem vários tipos de blocos, os mais comuns, são os blocos de códigos,
isto é, blocos que contenham instruções Python.

Outro tipo comum de bloco são os blocos de comentários, isto é, um conjunto de caracteres, que ocupam uma ou
mais linha de código e estão delimitados por uma notação que a linguagem de programação definiu.

Bloco de código é uma ou um conjunto de instrução que estejam numa mesma distância da margem esquerda.
É comum utilizarmos 2 espaços ou então, 4 espaços, ou mesmo 1 tabulação ao lado esquerdo da instrução
para assim definir, em qual bloco a instrução está contida. O primeiro nível é o nível 0, ou seja,
o nível que não contém espaçamento. A linguagem não nos obriga a utilizar uma determinada quantidade
de espaçamentos, ou então, tabulações. Porém, se utilizarmos 4 espaços para definir o primeiro blocos, o
interpretador assumirá que as próximas instruções estão indentadas com uso de múltiplos de 4.

A recomendação é que utilizemos, ou 1 tabulação, ou então, 4 espaços.

Ao invés de trabalharmos com quantidades de espaços, podemos utilizar uma determinada quantidade de tabulações.
O primeiro nível hierárquico seria o nível 0, isto é, instruções que não possuem tabulações a sua esquerda.
O segundo nível utilizaria uma única tabulação, o terceiro nível utilizaria 2 tabulações e assim sucessivamente.


2) De que maneira pode representar os valores booleanos True e False?

Existem dois tipos de inteiros: [...] inteiros (int) [...] booleanos (bool).

Em Python 3.x True e False são palavras-chave e sempre serão iguais a 1 e 0.
Booleanos: Representam os valores de verdade. Os valores False e True [...] Boolean se comportam como
os valores 0 e 1, respectivamente, em quase todos os contextos, exceto quando convertidos para uma string,
as strings "False" ou "True "são retornados, respectivamente.
Então booleanos são explicitamente considerados como inteiros em Python 2.6 e 3.
Em circunstâncias normais em Python 2, e sempre em Python 3: O objeto False é do tipo bool, que é uma subclasse de int:
object - int - bool


3) Que tipos de instruções condicionais existem e como se distinguem?

Existem três tipos de instruções de controle: sequências, condicionais e ciclos.

a) Sequências: recorre-se à delimitadores, como a tecla enter, ponto e vírgula, [], /\ etc. atribuição (soma e produto) e
impressão.

b) Condicionais: Programas escritos com estrutura de controle sequencial geralmente são pobres e resolvem
problemas muito simples. Há 3 categorias de condicionais: simples (uma via), normal (duas vias) e geral (várias vias).

condicional simples: em um teste com duas alternatvas, em apenas uma delas executamos ações e na outra nada fazemos;
ex: if-then
if <condição>:
    <corpo>

condicional normal: duas alternativas, ambas com ações para realizar. se a condição booleana for verdadeira, executamos
o <corpo1>, caso contrário, executamos o <corpo2>.
ex: if-else

if <condição>:
    <corpo>
else:
    <corpo>

condicional geral: permite-se um número variável de vias de decisão. Várias alternativas vão sendo percorridas por ordem
descendente e a primeira condição que for verdadeira desencadeia a execução de instruções associadas. Caso nenhuma seja
verdadeira, serão ativadas as instruções do ramo else.
ex: if-elif-else
if <condição>:
    <corpo>
elif <condição>:
    <corpo>
else <condição>:
    <corpo>


4) Qual é a diferença fundamental entre um ciclo for e um ciclo while?

for vai executar as instruções através de uma sequência conhecida for (i = 0; i < 10; i++) -
percorrer listas, vetores, executar um número definido x de ações e outros. Enquanto o while vai executar as
instruções até que a(s) condição(ões) seja(m) atendida(s) while (check).

A performance depende claramente da aplicação em particular e do compilador da linguagem utilizada.

Em C#, FOR é um pouco mais rápido. FOR teve uma média de 2,95-3,02 ms. O While média de cerca de 3,05-3,37 ms.

O laço for é geralmente usado quando você sabe o número de iterações de antemão. Por exemplo para percorrer um array
de 10 elementos que você pode usar para loop e incrementar o contador 0-9 (ou 1 a 10). Por outro lado while é
usado quando você tem uma idéia sobre a faixa de valores em que para fazer uma iteração, mas não sei o número
exato de iterações que ocorrem.

Além disso, o FOR é mais uma conveniência que um construtor de linguagem. Por exemplo, um FOR ser
facilmente expandido em um loop while.

O FOR não está limitado a operações numéricas simples, você pode fazer coisas mais complexas
5) De que modo pode percorrer um ciclo?


6) Que formas tem de interromper / quebrar um ciclo?

As instruções break, continue e pass em Python permitem que você use loops for
e while com maior efetividade em seu código.

a) BREAK - oferece a possibilidade de SAIR de um loop quando uma condição externa é acionada.
A instrução break será colocada dentro do bloco de código abaixo da sua instrução de loop,
geralmente após uma instrução condicional if.

number = 0

for number in range(10):
    if number == 5:
        break    # break here

    print('Number is ' + str(number))

print('Out of loop')

Neste pequeno programa, o number da variável é inicializado em 0. Em seguida, uma instrução for constrói o loop,
desde que o number da variável seja menor que 10.

Dentro do loop for, há uma instrução if que apresenta a condição que se o number da variável for equivalente ao número
inteiro 5, então o loop será quebrado.

Dentro do loop também há uma instrução print() que será executada com cada iteração do loop for até que o loop
seja quebrado, uma vez que está localizada após a instrução break. A instrução break faz com que um programa
seja interrompido para fora de um loop.

Para saber quando estamos fora do loop, incluímos uma instrução final print() fora do loop for.

b) CONTINUE - dá a opção de IGNORAR a parte de um loop onde uma condição externa é acionada,
mas continuar e completar o resto do loop. Ou seja, a iteração atual do loop será interrompida,
mas o programa retornará ao topo do loop.

ficará dentro do bloco de código abaixo da instrução de loop, geralmente após uma instrução condicional if.

number = 0

for number in range(10):
    if number == 5:
        continue    # continue here

    print('Number is ' + str(number))

print('Out of loop')

Aqui, Number is 5 nunca ocorre no resultado, mas o loop continua após esse ponto e imprime linhas para os
números 6-10 antes de ser finalizado.
Você pode usar a instrução continue para evitar um código condicional extremamente aninhado,
ou para otimizar um loop, eliminando casos que ocorram com frequência e que você gostaria de rejeitar.
A instrução continue faz com que um programa pule certos fatores que surjam dentro de um loop,
mas depois continuem pelo restante do loop.

c) PASS - permite lidar com a condição sem que o loop seja impactado; todo
o código continuará sendo lido a menos que um break ou outra instrução ocorra. ficará dentro do bloco de
código abaixo da instrução de loop, normalmente após uma instrução condicional if.

number = 0

for number in range(10):
    if number == 5:
        pass    # pass here

    print('Number is ' + str(number))

print('Out of loop')

Ao usar a instrução pass neste programa, notamos que o programa é executado exatamente como seria se não
houvesse nenhuma instrução condicional no programa. A instrução pass diz ao programa para desconsiderar
essa condição e continuar executando o programa como sempre.

A instrução pass pode criar classes mínimas, ou agir como um espaço reservado enquanto estamos
trabalhando em novos códigos e pensando em um nível algorítmico antes de construir detalhes.


7) Em que princípios se baseia o método de Monte Carlo?

Qualquer método de uma classe de métodos estatísticos que se baseiam em amostragens aleatórias massivas
para obter resultados numéricos. Em suma, utilizam a aleatoriedade de dados para gerar um resultado
para problemas que a priori são determinísticos. São utilizados mais comumente em problemas de física
e de matemática onde são muito difíceis ou impossível de serem resolvidos com outros métodos.
Tem sido utilizado há muito tempo como forma de obter aproximações numéricas de funções complexas em
que não é viável, ou é mesmo impossível, obter uma solução analítica ou, pelo menos, determinística.

Podem ser usados para resolver quaisquer problemas com um interpretação probabilística.

Exemplo:

import numpy as np

N = 100000 # número de iterações
n = 0
#gerando as coordenadas dos pontos no quadrado unitário seguindo uma distribuição uniforme entre 0 e 1.

x = np.random.uniform(size=N)
y = np.random.uniform(size=N)

#percorrendo as listas geradas de x e y, se o ponto gerado estiver dentro do primeiro quadrante do círculo, somo 1 no contador n.
for i in range(N):
    if x[i]**2 + y[i]**2 < 1:
        n+=1
#como a área de um quadrante do círculo é pi/4, multiplicamos a razão n/N por 4


8) Que diferenças existem entre exceções e asserções?

Existem dois tipos de erros: erros de sintaxe e exceções.

Em sintaxe (parse): O parser repete a linha inválida e apresenta uma pequena ‘seta’ apontando para o ponto da
linha em que o erro foi detectado.

Em exceções: O parser repete a linha inválida e apresenta uma pequena ‘seta’ apontando para o ponto da linha
em que o erro foi detectado. A parte anterior da mensagem de erro apresenta o contexto onde ocorreu a exceção.
Essa informação é denominada stack traceback (situação da pilha de execução).

>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero

>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined

>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't convert 'int' object to str implicitly

É possível escrever programas que tratam exceções específicas.

>>> while True:
...     try:
...         x = int(input("Please enter a number: "))
...         break
...     except ValueError:
...         print("Oops!  That was no valid number.  Try again...")

A instrução try funciona da seguinte maneira:

_ Primeiramente, a cláusula try (o conjunto de instruções entre as palavras reservadas try e except) é executada.

_ Se nenhuma exceção ocorrer, a cláusula except é ignorada e a execução da instrução try é finalizada.

_ Se ocorrer uma execução durante a execução da cláusula try, as instruções remanescentes na cláusula são ignoradas.
Se o tipo da exceção ocorrida tiver sido previsto em algum except, então essa cláusula será executada.
Depois disso, a execução continua após a instrução try.

_ Se a exceção levantada não foi corresponder a nenhuma exceção listada na cláusula de exceção, então ela é
entregue a uma instrução try mais externa. Se não existir nenhum tratador previsto para tal exceção, trata-se
de uma exceção não tratada e a execução do programa termina com uma mensagem de erro.

... except (RuntimeError, TypeError, NameError):
...     pass

A instrução assert existe em quase todas as linguagens de programação. Ele ajuda a detectar problemas
no início do programa, onde a causa é clara, e não mais tarde, como um efeito colateral de alguma outra operação.

Quando você faz...
assert condition
você está dizendo ao programa para testar essa condição e imediatamente acionar um erro se a condição for falsa.

if not condition:
    raise AssertionError()

ou:
assert False, "Oh no! This assertion failed!"

Do not use parênteses para chamar assert como uma função. É uma declaração. Se
você executar assert(condition, message), estará executando o assert com um (condition, message)
Tuple como primeiro parâmetro.

Quanto a desativá-los, ao executar python no modo otimizado, onde __debug__ é False, as instruções de
declaração serão ignoradas. Basta passar o sinalizador -O:
python -O script.py

'''