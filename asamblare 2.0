from Tkinter import *
import random
import time

tk = Tk()
tk.title("Car movement simulation")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=1300, height=700, bd=0, highlightthickness=0)
canvas.pack()
tk.update()
deplasareX=100
deplasareY=245
val2=0
val=True

class Semafor:
    def __init__(self, canvas, color,x,y):
        self.x = x
        self.y = y
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, x, y)
     
    def draw(self):
        self.canvas.move(self.id, 0, 0)

class Car:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(50, 50, 25, 25, fill=color)
        self.canvas.move(self.id, deplasareY, deplasareX)

  # daca e 1 se misca in jos, daca e -1 se misca in sus
  
    def goright(self):
        self.canvas.move(self.id, 1, 0)

    def godown(self):
        self.canvas.move(self.id, 0, 1)
        
car = Car(canvas, 'red')
semafor = Semafor(canvas, 'red',650,350)
semafor2 = Semafor(canvas, 'green',650,380)
semafor2 = Semafor(canvas, 'yellow',680,350)
semafor2 = Semafor(canvas, 'black',680,380)

while True:
    if (deplasareX<400):
        deplasareX=deplasareX+1
        car.goright()
    elif (deplasareY<500):
        deplasareY=deplasareY+1
        car.godown()
    else:
        car.goright()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
 

    val2 = val2 +1
    if(val2 == 30 and val == True):
        val2=0
        semafor=Semafor(canvas,'green',650,350)
        val =False
    if(val2 == 30 and val == False):
        val2=0
        semafor=Semafor(canvas,'red',650,350)
        val=True

#masini : 

tk = Tk()
tk.title("Car movement simulation")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=1300, height=700, bd=0, highlightthickness=0)
canvas.pack()
tk.update()
deplasareX=100
deplasareY=245

class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)

  # daca e 1 se misca in jos, daca e -1 se misca in sus
  
    def draw(self):
        self.canvas.move(self.id, 1, 0)
        
ball = Ball(canvas, 'red')

while 1:

    ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
