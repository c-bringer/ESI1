import tkinter

start = tkinter.Tk()
canvas = tkinter.Canvas(start, bg = "black", height = 500, width = 500)
canvas.pack()

canvas.create_oval(80, 80, 50, 50, outline="#f11", fill="#1f1", width=2)
canvas.create_oval(300, 300, 100, 100, outline="#f11", fill="#572826", width=2)

start.mainloop()