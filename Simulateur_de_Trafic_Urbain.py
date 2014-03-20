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

#definire canvas/interfata
tk = Tk()
tk.title("Simulateur de trafic urbain")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width = 1000, height = 700, bd = 0, highlightthickness = 0)
canvas.pack()
tk.update()

#cream obiect semafor + setam dimensiuni
class Semafor:
    def __init__(self, canvas, color,x,y):
        self.x = x
        self.y = y
        self.canvas = canvas
        self.id = canvas.create_oval(50, 50, 25, 25, fill=color)
        self.canvas.move(self.id, x, y)
     
    def draw(self):
        self.canvas.move(self.id, 0, 0)
        
#cream obiect car + setam dimensiuni
class Car:
    def __init__(self, canvas, color,x,y):
        self.x = x
        self.y = y
        self.canvas = canvas
        self.id = canvas.create_rectangle(75, 75, 25, 25, fill=color)
        self.canvas.move(self.id, x, y)

    #daca e 1 se misca in jos, daca e -1 se misca in sus
    def goright(self, x):
        for i in range(x):
            self.canvas.move(self.id, 1, 0)
            
    def godown(self):
        self.canvas.move(self.id, 0, 1)

def ThreadGenerareMasini():
    global stanga,sus
    
    #algoritmul de generare de masini
    #cream timerul in care se adauga masini in coada
    time_start = time.time()
    seconds = 0

    while True:  
        print'coada de sus contine: ', sus.queue,'\n'
        print'coada de stanga contine: ',stanga.queue,'\n'
        
        #la un interval de 2 sec apare o masina in intersectie
        if(seconds == 2):
            seconds =0
            randomValue=randint(0,10)
            
            #verificam daca este full coada (maxsize=4) + punem elemente in ea 
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
        
        #setam semaforul sa isi interschimbe culorile in intervale de 6 sec
        if(timpSemafor == 6):
            timpSemafor = 0
            aux = semaforSus
            semaforSus = semaforStanga
            semaforStanga= aux
            print 'semafor sus: ',semaforSus,'\n'
            print 'semafor jos: ',semaforStanga,'\n'

def ThreadTransferMasini():
    global semaforSus,semaforStanga,sus,stanga,jos,dreapta,maxsize
    
    #adaugam elementele din coada 'stanga', respectiv 'sus', in functie de valoarea 'semaforStanga', 'semaforSus', in coada 'dreapta' si in coada 'jos'
    #in cazul in care cozile 'dreapta' sau 'sus' ajung la valoarea maxima 4, insertia elementelor in aceste cozi este blocata pana la eliberarea lor
    while True:
        if(semaforStanga == True and stanga.qsize() != 0):
            dreapta.put(stanga.get(0))
            print 'coada de stanga contine: ',stanga.queue,'\n'
        if(semaforSus == True and sus.qsize() != 0):
           jos.put(sus.get(0))
           print 'coada de jos contine: ',jos.queue,'\n'
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
    
    #folosim aceasta functie pe post de Queue.get() pentru golirea cozilor 'dreapta' si 'jos', in locul utilizarii unui ThreadStergereMasini()
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

    #setam cele 2 valori pe care le pot lua semafoarele in functie de culori + setam coordonatele acestora
    if(semaforSus == True):
        semafor_sus = Semafor(canvas, 'green',390,240)
    else:
        semafor_sus = Semafor(canvas, 'red',390,240)
    if(semaforStanga == False):
        semafor_stanga=Semafor(canvas,'red',390,385)
    else:
        semafor_stanga=Semafor(canvas,'green',390,385)

    #setam coordonatele pe care se pot pozitiona masinile/elementele din cadrul cozilor in contextul interfetei, in functie de (width = 1000) si (height = 700)
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

   
