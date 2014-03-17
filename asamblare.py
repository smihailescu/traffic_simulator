import Tkinter
from Tkinter import *
import random
import time


#background : 

root = Tkinter.Tk()
canvas = Tkinter.Canvas(root, width = 1300, height = 700)
canvas.grid(row=0, column =0)
photo = Tkinter.PhotoImage(file = './background.gif')
canvas.create_image(650,350, image=photo)
root.mainloop()

#semafor : 

"""tk = Tk()
tk.title("Simulator")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)"""
#canvas.pack()
#tk.update()
val2=0
val=True
class Semafor:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.draw(self.id, 245, 100)
        
    """def draw(self):
        self.canvas.move(self.id, 0, 0)"""
        
semafor = Semafor(canvas, 'red')

while 1:
    
    #semafor.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(1)
    val2 = val2 +1
    if(val2 == 3 and val == True):
        val2=0
        semafor=Semafor(canvas,'green')
        val =False
    if(val2 == 3 and val == False):
        val2=0
        semafor=Semafor(canvas,'red')
        val=True




"""

#car :

class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, deplasareY, deplasareX)

  # daca e 1 se misca in jos, daca e -1 se misca in sus
  
    def draw(self):
        self.canvas.move(self.id, 1, 0)
        
ball = Ball(canvas, 'red')

while 1:
    deplasareX = deplasareX +20
    deplasareY = deplasareY +20
   # if( == 400):
    #    deplasareY = 0
     #   deplasareX = 0
    ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
"""
