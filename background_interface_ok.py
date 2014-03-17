import Tkinter

root = Tkinter.Tk()
canvas = Tkinter.Canvas(root, width = 1300, height = 700)
canvas.grid(row=0, column =0)
photo = Tkinter.PhotoImage(file = './background.gif')
canvas.create_image(650,350, image=photo)
root.mainloop()
