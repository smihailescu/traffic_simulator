from Tkinter import *
import random
import time

tk = Tk()
tk.title("Car movement simulation")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=1000, height=700, bd=0, highlightthickness=0)
canvas.pack()
tk.update()
deplasareX=350
deplasareY=450
val2=0
val=True

#linii orizonatle     
canvas.create_line(0, 300, 450, 300)              
canvas.create_line(550, 300, 1000, 300)
canvas.create_line(0, 400, 450, 400)     
canvas.create_line(550, 400, 1000, 400)

#linii verticale
canvas.create_line(450, 0, 450, 300)
canvas.create_line(550, 0, 550, 300)
canvas.create_line(450, 400, 450, 700)
canvas.create_line(550, 400, 550, 700)

class Semafor:
    def __init__(self, canvas, color,x,y):
        self.x = x
        self.y = y
        self.canvas = canvas
        self.id = canvas.create_oval(50, 50, 25, 25, fill=color)
        self.canvas.move(self.id, x, y)
     
    def draw(self):
        self.canvas.move(self.id, 0, 0)

class Car:
    def __init__(self, canvas, color,x,y):
        self.x = x
        self.y = y
        self.canvas = canvas
        self.id = canvas.create_rectangle(75, 75, 25, 25, fill=color)
        self.canvas.move(self.id, x, y)

  # daca e 1 se misca in jos, daca e -1 se misca in sus
  
    def goright(self):
        self.canvas.move(self.id, 1, 0)

    def godown(self):
        self.canvas.move(self.id, 0, 1)

 #cream masina pe stanga       
car1 = Car(canvas, 'Dark Green', 0, 300)
#cream masina pe dreapta
car2 = Car(canvas, 'Seashell', 450, 0)

semafor=Semafor(canvas,'red',390,385)
semafor2 = Semafor(canvas, 'green',390,240)


while True:
    
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
    val2 = val2 +1
    if(val2 == 200 and val == True):
        val2=0
        semafor=Semafor(canvas,'green',390,385)
        semafor2 = Semafor(canvas, 'red',390,240)
        val =False
    if(val2 == 200 and val == False):
        val2=0
        semafor=Semafor(canvas,'red',390,385)
        semafor2 = Semafor(canvas, 'green',390,240)
        val=True


