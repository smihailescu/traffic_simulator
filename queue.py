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


time_start = time.time()
seconds = 0

while True:
    try:
        if(seconds == 5):
            seconds =0
            randomValue=randint(0,10)
            print 'random= ',randomValue
            if(randomValue > 3 ):
                sus.put(1)
                jos.put(1)
                stanga.put(1)
                dreapta.put(1)
                sus.queue
                jos.queue
                stanga.queue
                dreapta.queue
                
        seconds = seconds +1
        print seconds
        time.sleep(1)
    except KeyboardInterrupt, e:
        break
