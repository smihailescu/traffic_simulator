from Tkinter import *
import random
import time

tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()
val2=0
val=True
class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        
    def draw(self):
        self.canvas.move(self.id, 0, 0)
        
ball = Ball(canvas, 'red')

while 1:
    
    ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(1)
    val2 = val2 +1
    if(val2 == 3 and val == True):
        val2=0
        ball=Ball(canvas,'green')
        val =False
    if(val2 == 3 and val == False):
        val2=0
        ball=Ball(canvas,'red')
        val=True
