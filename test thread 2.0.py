import time
import threading
from random import randint
import Queue

#cozile noastre

maxsize=4 #dimensiunea cozilor noastre
sus = Queue.Queue(maxsize)     #in coada de sus si stanga sunt generate masini
stanga = Queue.Queue(maxsize)  #in coada de sus si stanga sunt generate masini
jos = Queue.Queue(maxsize)     #in coada de jos si dreapta primesc masini de la stanga si sus
dreapta = Queue.Queue(maxsize) #in coada de jos si dreapta primesc masini de la stanga si sus

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
        if(semaforStanga == True and stanga.qsize() != 0):
            dreapta.put(stanga.get(0))
            print 'coada de stanga arata cam asa: ',stanga.queue,'\n'
        if(semaforSus == True and sus.qsize() != 0):
           jos.put(sus.get(0))
           print 'coada de jos arata cam asa: ',jos.queue,'\n'
           

t1 = threading.Thread(target=ThreadGenerareMasini, args=[])
t2 = threading.Thread(target=ThreadSemafoare, args=[])
t3 = threading.Thread(target=ThreadTransferMasini, args=[])

t1.start()
t2.start()
t3.start()
