import turtle
import time

# Pencere oluşturma
win = turtle.Screen()
win.title("Breakout Game")
win.bgcolor("black")
win.setup(width=600, height=600)

# Paleti oluşturma
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Topu oluşturma
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 3 # Topun x ekseni hareket hızı
ball.dy = -3  # Topun y ekseni hareket hızı

# Blokları oluşturma
blocks = []
colors = [
    "Orange", "OrangeRed", "Orchid", "PaleGoldenrod", "PaleGreen", "PaleTurquoise", "PaleVioletRed",
    "PapayaWhip", "PeachPuff", "Peru", "Pink", "Plum", "PowderBlue", "Purple", "Red", "RosyBrown",
    "RoyalBlue", "SaddleBrown", "Salmon", "SandyBrown", "SeaGreen", "SeaShell", "Sienna", "Silver",
    "SkyBlue", "SlateBlue", "SlateGray", "Snow", "SpringGreen", "SteelBlue",
    "Turquoise", "Violet", "Wheat", "White", "Yellow", "Orange", "OrangeRed", "Orchid", "PaleGoldenrod", "PaleGreen", "PaleTurquoise", "PaleVioletRed",
    "PapayaWhip"
]
x_pos = -250  # Başlangıç x pozisyonu
y_pos = 250
for color in colors:
    block = turtle.Turtle()
    if block.xcor() <= 270:
        block.shape("square")
        block.color(color)
        block.shapesize(stretch_wid=1, stretch_len=2)  # Blok boyutları
        block.penup()
        block.goto(x_pos, y_pos)  # Blok pozisyonu
        blocks.append(block)
        x_pos += 55
    if block.xcor() >= 270:
        y_pos -= 55
        x_pos = -250
        block.shape("square")
        block.color(color)
        block.shapesize(stretch_wid=1, stretch_len=2)
        block.penup()
        block.goto(x_pos, y_pos)
        blocks.append(block)
# Paleti hareket ettirme
def paddle_right():
    x = paddle.xcor()
    if x < 225:
        x += 20
    paddle.setx(x)

def paddle_left():
    x = paddle.xcor()
    if x > -225:
        x -= 20
    paddle.setx(x)

# Tuş dinleme
win.listen()
win.onkeypress(paddle_right, "Right")
win.onkeypress(paddle_left, "Left")

# Oyun döngüsü
while True:
    win.update()

    # Topu hareket ettirme
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Duvar çarpışmaları
    if ball.xcor() > 290 or ball.xcor() < -290:
        ball.dx *= -1

    if ball.ycor() > 290:
        ball.dy *= -1

    # Palet çarpışması
    if (ball.ycor() < -240 and ball.ycor() > -250) and (ball.xcor() < paddle.xcor() + 50 and ball.xcor() > paddle.xcor() - 50):
        ball.sety(-240)
        ball.dy *= -1

    # Blok çarpışmaları
    for block in blocks:
        if block.distance(ball) < 20:
            block.goto(500, 500)  # Bloğu ekrandan uzaklaştırma
            ball.dy *= -1

    # Oyun bitişi
    if ball.ycor() < -290:
        ball.goto(0, 0)
        ball.dy *= -1
        for block in blocks:
            block.goto(-250, 200 - blocks.index(block) * 30)
            block.showturtle()
        time.sleep(1)

win.mainloop()
