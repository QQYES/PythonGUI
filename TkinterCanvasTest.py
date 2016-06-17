# coding=utf-8
from Tkinter import *

window = Tk()
canvas = Canvas(window, width=200, height=100, bg="white")
canvas.pack()
# canvas.create_rectangle(10, 10, 190, 90, tags="rect")
canvas.create_oval(10,10,190,90,fill="red",tags="oval")
# canvas.create_arc(10,10,190,90,start=0,extent=90,width=8,fill="red",tags="arc")
# canvas.create_polygon(10,10,190,90,30,50,tags="poly")
# canvas.create_line(10,90,190,10,width=9,arrow="last",activefill="blue",tags="line")
# canvas.create_text(60,40,text="string",font="Times 10 bold underline",tags="string")
# canvas.delete("rect","oval","arc","poly","line","string")
window.mainloop()
