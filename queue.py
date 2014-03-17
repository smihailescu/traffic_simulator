from random import randint
import Queue
import time

#dimensiunea maxima a cozilor
maxsize=10

#cozile noastre
sus = Queue.Queue(maxsize)
jos = Queue.Queue(maxsize)
stanga = Queue.Queue(maxsize)
dreapta = Queue.Queue(maxsize)

#cream semaforul
class Traffic_Light:
 def __init__(self, light):
     self.light=light
 def __str__(self):
     return "Traffic light {"+str(self.light)+"}"

semafor_sus=Traffic_Light(True)
semafor_stanga=Traffic_Light(False)

#cream timerul in care se adauga masini in coada
time_start = time.time()
seconds = 0
while True:
    try:
        if(seconds == 5):
            seconds =0
            randomValue=randint(0,10)
            print 'random= ',randomValue
            if(randomValue > 3 ):
                if (sus.full() == False):
                    sus.put(1)
                if (stanga.full() == False):
                    stanga.put(1)
                print sus.queue
                print stanga.queue        
        seconds = seconds +1
        print seconds
        time.sleep(1)
    except KeyboardInterrupt, e:
        break
    
#cream timer pentru semafoare 
time_start = time.time()
seconds = 0
#executa codul urmator forever
while True:
    try:
        if(seconds == 7):
            seconds=0
            semafor_sus.light= not(semafor_sus.light)
            semafor_stanga.light= not(semafor_stanga.light)
        seconds = seconds +1
        time.sleep(1)
    except KeyboardInterrupt, e:
        break
