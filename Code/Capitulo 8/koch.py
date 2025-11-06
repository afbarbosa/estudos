import turtle

def setup(pencil):
    pencil.color('blue')
    pencil.penup()
    pencil.goto(-300,100)
    pencil.pendown()

def koch(pencil,size,order):
    if order == 0:
        pencil.forward(size)
    else:
        for angle in [90,-90,-90,90,0]:
            koch(pencil, size/4, order-1)
            pencil.left(angle)
            print(order)

def main():
    pencil = turtle.Turtle()
    setup(pencil)

    order = 3
    size = 600
    koch(pencil,size,order)

if __name__ == '__main__':
    main()
    turtle.tracer(100)
    turtle.mainloop()
