import random
import turtle

def visualiza(pontos):

    turtle.setworldcoordinates(-2, -2, 2, 2)
    janela = turtle.Turtle()
    janela.hideturtle()

    janela.up
    janela.goto(-1, 0)
    janela.down()
    janela.goto(1, 0)

    janela.up()
    janela.goto(0,1)
    janela.down()
    janela.goto(0, -1)

    janela.up()
    janela.goto(0, -1)
    janela.down()
    janela.circle(1, steps = 360)

    janela.up()
    janela.goto(-1, -1)
    janela.down()

    for i in range(4):
        janela.forward(2)
        janela.left(90)
    janela.up()

    for elem in pontos:
        x, y = elem
        d = (x**2 + y**2) ** 0.5
        if d <= 1:
            janela.color("blue")
        else:
            janela.color("red")
        janela.goto(x, y)
        janela.dot()

def monte_carlo_pi(num_dardos):

    conta_dardos_in = 0.0
    tuplos_dardos = tuple()

    for i in range(num_dardos):

        x = random.random()
        y = random.random()
        tuplos_dardos += ((x,y),)

        d = (x**2 + y**2) ** 0.5
        if d <= 1:
            conta_dardos_in = conta_dardos_in + 1
    res_pi = 4 * (conta_dardos_in / num_dardos)
    print(res_pi)
    return tuplos_dardos

if __name__ == '__main__':
    dardos = monte_carlo_pi(1500)
    visualiza(dardos)
    turtle.exitonclick()