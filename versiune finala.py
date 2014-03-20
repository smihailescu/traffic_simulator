from Tkinter import *
from random import *
import time
import Queue
import threading

#cream cozile
maxsize=4
sus = Queue.Queue(maxsize)
jos = Queue.Queue(maxsize)
stanga = Queue.Queue(maxsize)
dreapta = Queue.Queue(maxsize)

#declararea semafoarelor
semaforSus=True
semaforStanga=False
#variabila care va face swich-ul de culori intre semafoare (alterneaza 7 sec)
timpSemafor=0



tk = Tk()
tk.title("Car movement simulation")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=1000, height=700, bd=0, highlightthickness=0)
canvas.pack()
tk.update()




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
#car1 = Car(canvas, 'Dark Green', 0, 300)
#cream masina pe dreapta
#car2 = Car(canvas, 'Seashell', 450, 0)

#cream semaforul de sus
#semafor_sus = Semafor(canvas, 'green',390,240)
#cream semaforul din stanga
#semafor_stanga=Semafor(canvas,'red',390,385)

def ThreadGenerareMasini():
    global stanga,sus
    #algoritmul de generare de masini
    #cream timerul in care se adauga masini in coada
    time_start = time.time()
    seconds = 0
    
    while True:
        
        #print'coada de sus arata cam asa: ', sus.queue,'\n'
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
        if(timpSemafor == 3):
            timpSemafor = 0
            aux = semaforSus
            semaforSus = semaforStanga
            semaforStanga= aux
            print 'semafor sus: ',semaforSus,'\n'
            print 'semafor jos: ',semaforStanga,'\n'

def ThreadTransferMasini():
    global semaforSus,semaforStanga,sus,stanga,jos,dreapta,maxsize
    while True:
        if(semaforStanga == True and stanga.qsize() != 0):
            dreapta.put(stanga.get(0))
            print 'coada de stanga arata cam asa: ',stanga.queue,'\n'
        if(semaforSus == True and sus.qsize() != 0):
           jos.put(sus.get(0))
           print 'coada de jos arata cam asa: ',jos.queue,'\n'
        if(jos.qsize() == maxsize):
            jos = Queue.Queue(maxsize)
        if(dreapta.qsize() == maxsize):
            dreapta = Queue.Queue(maxsize)
           

t1 = threading.Thread(target=ThreadGenerareMasini, args=[])
t2 = threading.Thread(target=ThreadSemafoare, args=[])
t3 = threading.Thread(target=ThreadTransferMasini, args=[])

t1.start()
t2.start()
t3.start()


while True:
    #legatura dintre grafica semafoarelor si threadul cu semafoare
    canvas.delete("all")

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
    
    if(semaforSus == True):
        semafor_sus = Semafor(canvas, 'green',390,240)
    else:
        semafor_sus = Semafor(canvas, 'red',390,240)
    if(semaforStanga == False):
        semafor_stanga=Semafor(canvas,'red',390,385)
    else:
        semafor_stanga=Semafor(canvas,'green',390,385)

    for i in range(stanga.qsize()):
        car = Car(canvas, 'blue', 300 - i*100, 300)

    for i in range(sus.qsize()):
        car = Car(canvas, 'blue', 450, 210 - i*70)

    for i in range(dreapta.qsize()):
        car = Car(canvas, 'blue', 900 - i*100, 300)

    for i in range(jos.qsize()):
        car = Car(canvas, 'blue', 450, 590 - i*70)
    
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

   
