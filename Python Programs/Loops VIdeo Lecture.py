import turtle
andy = turtle.Pen()
andy.forward(250)
andy.left(90)
andy.forward(50)
andy.left(90)
andy.forward(60)
andy.right(45)
andy.forward(55)
andy.left(45)
andy.forward(60)
andy.left(45)
andy.forward(55)
andy.right(45)
andy.forward(54)
andy.left(90)
andy.forward(50)
andy.left(90)
andy.forward(35)
andy.right(90)
andy.forward(25)
andy.left(90)
andy.forward(25)
andy.left(90)
andy.forward(25)
andy.right(90)
andy.forward(130)
andy.right(90)
andy.forward(25)
andy.left(90)
andy.forward(25)
andy.left(90)
andy.forward(25)
andy.right(90)
andy.reset()
for i in range(8):
    andy.forward(100)
    andy.left(120)


andy.reset()
for i in range(8):
    andy.forward(100)
    andy.left(225)


for i in range(5):
    print(i)


andy.reset()
for i in range(10):
    andy.forward(20 * i)
    andy.left(90)
andy.reset()
andy.speed(0)
for i in range(50):
    andy.circle(i * 3)
    andy.left(10)


andy.reset()
andy.speed(0)
andy.color("yellow")
andy.width(4)
for i in range(20):
    andy.circle(1*3, 180)
    andy.right(45)


andy.reset()
andy.speed(10)
andy.color("black")
for i in range(1):
    andy.circle(1 * 20)
    andy.left(10)
    andy.left(85)
    andy.color("white")
    andy.forward(50)
    andy.color("black")

    
    

    

