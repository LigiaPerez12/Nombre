import time
from tkinter import*
tk=Tk()
my_image= PhotoImage(file="ball.gif")
canvas=Canvas(tk, width=400, height=200)
canvas.pack()
canvas.create_polygon(10, 10 ,10 ,60, 50,35)
for x in range(0, 60):
	canvas.move(1,2,4)
	tk.update()
	time.sleep(0.05)

tk.mainloop()