import time
import threading
from random import randint
import Queue
from Tkinter import *

#cozile noastre

maxsize=4 #dimensiunea cozilor noastre
sus = Queue.Queue(maxsize)     #in coada de sus si stanga sunt generate masini
stanga = Queue.Queue(maxsize)  #in coada de sus si stanga sunt generate masini
jos = Queue.Queue(maxsize)     #in coada de jos si dreapta primesc masini de la stanga si sus
dreapta = Queue.Queue(maxsize) #in coada de jos si dreapta primesc masini de la stanga si sus

tk = Tk()
tk.title("Car movement simulation")
tk.resizable(0, 0)
#tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=1000, height=700, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

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


#cream semaforul de sus
semaforSus = Semafor(canvas, 'green',390,240)
#cream semaforul din stanga
semaforStanga=Semafor(canvas,'red',390,385)


#declararea semafoarelor
semaforSus=True
semaforStanga=False
#variabila care va face swich-ul de culori intre semafoare (alterneaza 7 sec)
timpSemafor=0


def ThreadGenerareMasini():
    #algoritmul de generare de masini
    
    #cream timerul in care se adauga masini in coada
    time_start = time.time()
    seconds = 0
    
    while True:
        print'coada de sus arata cam asa: ', sus.queue,'\n'
        print'coada de stanga arata cam asa: ',stanga.queue,'\n'
        if(seconds == 2):
            seconds =0
            randomValue=randint(0,10)
            if(randomValue > 3 ):
                if (sus.full() == False):
                    sus.put(1)
                if (stanga.full() == False):
                    stanga.put(1)      
        seconds = seconds +1
        time.sleep(1)
   

    
def ThreadSemafoare():
    global semaforSus,semaforStanga
    timpSemafor = 0
    while True:
        time.sleep(1)
        timpSemafor =timpSemafor + 1
        if(timpSemafor == 7):
            timpSemafor = 0
            aux = semaforSus
            semaforSus = semaforStanga
            semaforStanga= aux
            print 'semafor sus: ',semaforSus,'\n'
            print 'semafor jos: ',semaforStanga,'\n'

def ThreadTransferMasini():
    global semaforSus,semaforStanga,sus,stanga,jos,dreapta
    while True:
        if(semaforStanga == True and not stanga.empty()):
            dreapta.put(stanga.get())
            print 'coada de dreapta arata cam asa: ',dreapta.queue,'\n'
        if(semaforSus == True and not sus.empty()):
           jos.put(sus.get())
           print 'coada de jos arata cam asa: ',jos.queue,'\n'

def ThreadStergereMasini():
    global dreapta,jos
    while True:
        if not dreapta.empty():
            dreapta.get()
        if not jos.empty():
            jos.get()
            
        timer.sleep(2)
    
        
t1 = threading.Thread(target=ThreadGenerareMasini, args=[])
t2 = threading.Thread(target=ThreadSemafoare, args=[])
t3 = threading.Thread(target=ThreadTransferMasini, args=[])
t4 = threading.Thread(target=ThreadStergereMasini, args=[])

t1.start()
t2.start()
t3.start()
t4.start()

while True:
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

    if (stanga.qsize()==0):
        stanga.put(1)
        car = Car(canvas, 'blue', 300, 300)
    elif (stanga.qsize()==1):
        car = Car(canvas, 'blue', 200, 300)
        stanga.put(1)
    elif (stanga.qsize()==2):
        car = Car(canvas, 'blue', 100, 300)
        stanga.put(1)
    else :
        car = Car(canvas, 'blue', 0, 300)
        stanga.put(1)
