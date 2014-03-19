from Tkinter import *
from random import *
import time
import Queue

#cream cozile
maxsize=4
sus = Queue.Queue(maxsize)
jos = Queue.Queue(maxsize)
stanga = Queue.Queue(maxsize)
dreapta = Queue.Queue(maxsize)

tk = Tk()
tk.title("Car movement simulation")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=1000, height=700, bd=0, highlightthickness=0)
canvas.pack()
tk.update()
deplasareX=350
deplasareY=450
val1=0
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
  
    def goright(self, x):
        for i in range(x):
            self.canvas.move(self.id, 1, 0)
            

    def godown(self):
        self.canvas.move(self.id, 0, 1)

#cream masina pe stanga       
car1 = Car(canvas, 'Dark Green', 0, 300)
#cream masina pe dreapta
car2 = Car(canvas, 'Seashell', 450, 0)

#cream semaforul de sus
semafor_sus = Semafor(canvas, 'green',390,240)
#cream semaforul din stanga
semafor_stanga=Semafor(canvas,'red',390,385)

while True:
    
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
    val1= val1+1
    val2 = val2 +1
   
#algoritmul de creare a masinilor in coada
    if(val1 == 300):
            val1=0
            randomValue=randint(0,10)
            if(randomValue > 3 ):
                if (stanga.full() == False):
                    if (stanga.qsize()==0):
                        car = Car(canvas, 'blue', 0, 300)
                        x=200
                        y=0
                        canvas.move(car,x,y)
                        canvas.update()
                        time.sleep(0.025)
                    #elif (stanga.qsize()==1):
                    #elif (sus.size==2):
                    #else (sus.size==3):
                #if (stanga.full() == False):
                    #stanga.put(1)       

#algoritmul de schimbare a culorii semaforului  
    if(val2 == 200 and val == True):
        val2=0
        semafor_stanga=Semafor(canvas,'green',390,385)
        semafor_sus = Semafor(canvas, 'red',390,240)
        
        val =False
    if(val2 == 200 and val == False):
        val2=0
        semafor_stanga=Semafor(canvas,'red',390,385)
        semafor_sus = Semafor(canvas, 'green',390,240)
        val=True
  

