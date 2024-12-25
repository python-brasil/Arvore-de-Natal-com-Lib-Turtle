import turtle

# Configuração inicial da tela
screen = turtle.Screen()
screen.bgcolor("sky blue")

# Criação da tartaruga para desenhar
t = turtle.Turtle()
t.shape("turtle")
t.speed(4)

# Função para desenhar um triângulo (parte da árvore de Natal)
def draw_triangle(color, size, position):
    t.penup()
    t.goto(position)
    t.pendown()
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(3):
        t.forward(size)
        t.left(120)
    t.end_fill()


# Desenho da árvore de Natal (triângulos)
draw_triangle("green", 200, (-100, -50))  # Base
draw_triangle("green", 160, (-80, 20))    # Meio
draw_triangle("green", 120, (-60, 80))    # Topo

# Desenhando o tronco da árvore
t.penup()
t.goto(-30, -50)
t.pendown()
t.color("brown")
t.begin_fill()
t.fillcolor("brown")
for _ in range(2):
    t.forward(60)
    t.right(90)
    t.forward(50)
    t.right(90)
t.end_fill()



# desenhar uma estrela
def draw_star(color, size, position):
    t.penup()
    t.goto(position)
    t.pendown()
    t.begin_fill()
    t.fillcolor(color)
    t.color(color)
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()


# Desenhando a estrela no topo da árvore (cor, tamanho, eixo lateral e eixo vertical)
draw_star("yellow", 40, (-20, 200)) 

# Função para desenhar uma mensagem
def draw_message(message, position):
    t.penup()
    t.goto(position)
    t.pendown()
    t.color("black")
    t.write(message, align="center", font=("Arial", 20, "bold"))


# Escrevendo a mensagem
draw_message("Python Brasil deseja a todos um feliz natal", (0, -200))

# Finalizando
t.hideturtle()
turtle.done()
