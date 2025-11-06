import turtle

rafael = turtle.Turtle()
rafael.shape('turtle')
rafael.pencolor('blue')
rafael.setposition(-120,0)
rafael.pendown()
rafael.circle(50)
#rafael.speed(1000)

rafael.pencolor('red')
rafael.setposition(120,0)
rafael.pendown()
rafael.circle(50)
##donatelo = turtle.Turtle()
##donatelo.shape('turtle')
##donatelo.color('purple')
##donatelo.speed(1000)

#def movimenta_tartaruga(tartaruga):
#    for i in range (0,5):
#        tartaruga.forward(100)
#        tartaruga.right(144)

##def mandala(tartaruga):
##    for i in range(0,36):
##        movimenta_tartaruga(tartaruga)
##        tartaruga.right(10)


#movimenta_tartaruga(rafael)
##donatelo.right(5)
##mandala(donatelo)

turtle.mainloop()
