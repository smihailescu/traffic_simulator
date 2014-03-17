from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtOpenGL import QGLWidget
from random import randint
import Queue
import time
import wx 

#dimensiunea maxima a cozilor
maxsize=10

#cozile noastre
sus = Queue.Queue(maxsize)
jos = Queue.Queue(maxsize)
stanga = Queue.Queue(maxsize)
dreapta = Queue.Queue(maxsize)

#cream semaforul
class Traffic_Light(QGraphicsEllipseItem):
 def __init__(self, light, parent=None):
     super(Traffic_Light,self).__init__(parent)
     self.radius=16
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
            if(randomValue > 5 ):
                if (sus.full() == False):
                    sus.put(1)
                if (stanga.full() == False):
                    stanga.put(1)      
        seconds = seconds +1
        time.sleep(1)
    except KeyboardInterrupt, e:
        break
    
#cream timer pentru semafoare 
time_start = time.time()
seconds = 0
#executa codul urmator forever
while True:
    try:
        if (semafor_sus.light== True):
            jos.put(sus.get(0))
        if (semafor_stanga.light== True):
            dreapta.put(stanga.get(0))
        if(seconds == 7):
            seconds=0
            semafor_sus.light= not(semafor_sus.light)
            semafor_stanga.light= not(semafor_stanga.light)
        seconds = seconds +1
        time.sleep(1)
    except KeyboardInterrupt, e:
        break



class MyFrame(wx.Frame): 
    def __init__(self, parent=None): 
        wx.Frame.__init__(self, parent)
        self.
        self.panel = wx.Panel(self, size=(1300, 700)) 
        self.panel.Bind(wx.EVT_PAINT, self.on_paint) 
        self.Fit() 

    def on_paint(self, event):
        # desenam cercul 
        dc = wx.PaintDC(self.panel)
        dc.SetBrush(wx.Brush('red'))
        x = 50
        y = 50
        r = 50
        dc.DrawCircle(x, y, r)


# testam 
app = wx.PySimpleApp() 
frame1 = MyFrame(title='Semafor_red') 
frame1.Center() 
frame1.Show() 
app.MainLoop()
