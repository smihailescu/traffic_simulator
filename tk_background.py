from Tkinter import *
     
canvas = Canvas(width=300, height=300, bg='white')  
canvas.pack(expand=YES, fill=BOTH)                  

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

#dashLine
canvas.create_line(xy, fill="black", dash=(2, 4))

#linii orizonatle
canvas.create_line(xy, fill="black", dash=(0, 350, 450, 350)
canvas.create_line(xy, fill="black", dash=(550, 350, 1000, 350)

#linii verticale                   
canvas.create_line(xy, fill="black", dash=(500, 0, 500, 300)
canvas.create_line(xy, fill="black", dash=(500, 400, 500, 700)                   


canvas.create_window(100, 100, window=widget)     
mainloop()
