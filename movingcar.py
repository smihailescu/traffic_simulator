from Tkinter import *
import random
import time

tk = Tk()
tk.title("Traffic simu")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()
deplasareX=100
deplasareY=245

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
