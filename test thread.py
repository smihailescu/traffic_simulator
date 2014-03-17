import time
import threading
from random import randint
import Queue

#cozile noastre

maxsize=10 #dimensiunea cozilor noastre
sus = Queue.Queue(maxsize)     #in coada de sus si stanga sunt generate masini
stanga = Queue.Queue(maxsize)  #in coada de sus si stanga sunt generate masini
jos = Queue.Queue(maxsize)     #in coada de jos si dreapta primesc masini de la stanga si sus
dreapta = Queue.Queue(maxsize) #in coada de jos si dreapta primesc masini de la stanga si sus





def ThreadGenerareMasini():
    #algoritmul de generare de masini
    
    #cream timerul in care se adauga masini in coada
    time_start = time.time()
    seconds = 0
    
    while True:
        print sus.queue
        print stanga.queue
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
    #declararea semafoarelor
    semaforSus=True
    semaforStanga=Falses
    while True:
        #print ' semafor '
        time.sleep(1)

def ThreadTransferMasini():
    while True:
       # print ' transfer '
        time.sleep(1)

t1 = threading.Thread(target=ThreadGenerareMasini, args=[])
t2 = threading.Thread(target=ThreadSemafoare, args=[])
t3 = threading.Thread(target=ThreadTransferMasini, args=[])

t1.start()
t2.start()
t3.start()
