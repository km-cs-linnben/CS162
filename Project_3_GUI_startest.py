"""
Ken Michna
Project 3
10/15/2022

I have no idea what I'm doing

Moveable UFO GUI with buttons to turn abduction beam on/off. Lots more I'd like to do but out of time again.
"""
import tkinter as tk
import random

root = tk.Tk()
root.title("UFO")

#Create blank canvas
canvas_output = tk.Canvas(root, width=640, height=480, background="black", highlightbackground="purple")
canvas_output.grid(column=0,row=4,columnspan=3)

#Tediously create a UFO
ufo = canvas_output.create_oval(110,10,250,50, fill="grey", outline="green", tags= "ufo")
ufo_window = canvas_output.create_rectangle(115,25,125,35, fill="black", outline="green", tags="ufo")
ufo_window1 = canvas_output.create_rectangle(145,25,155,35, fill="black", outline="green", tags="ufo")
ufo_window2 = canvas_output.create_rectangle(175,25,185,35, fill="black", outline="green", tags="ufo")
ufo_window3 = canvas_output.create_rectangle(205,25,215,35, fill="black", outline="green", tags="ufo")
ufo_window4 = canvas_output.create_rectangle(235,25,245,35, fill="black", outline="green", tags="ufo")

#loop to make stars background
for i in range(1,100):
    starpointx = random.randint(0,630)
    starpointy = random.randint(0,470)
    star = canvas_output.create_oval(starpointx,starpointy,starpointx+5,starpointy+5, fill="white")
    canvas_output.lower(star,"ufo")

def move_canvas_object(object_index, move_x, move_y):
    """Made into a function so buttons commands can do more than 1 thing at a time"""
    canvas_output.move(object_index, move_x, move_y)

def create_triangle():
    """Creates a triangle underneath UFO."""
    global yinc
    global xinc
    points = [180+xinc,50+yinc,230+xinc,250+yinc,130+xinc,250+yinc]   #points in x/y coords per point for creating a triangle
    my_triangle = canvas_output.create_polygon(points, fill="green2", outline="blue", tags="beam")
    canvas_output.lower(my_triangle,og_cow)   #lowers triangle image 1 layer below cow

#Create increments to help abduction beam follow UFO
yinc = 0
xinc = 0

def l_tri_incrementer():
    """Increments position left"""
    global xinc
    xinc -= 10

def r_tri_incrementer():
    """Increments position right"""
    global xinc
    xinc += 10

def u_tri_incrementer():
    """Increments position up"""
    global yinc
    yinc -= 10

def d_tri_incrementer():
    """Increments position down"""
    global yinc
    yinc += 10

ufo_moveup_bt = tk.Button(root, text="Up", command=lambda: [move_canvas_object("ufo", 0, -10), u_tri_incrementer()])
ufo_moveup_bt.grid(column=1,row=0)

ufo_moveup_bt = tk.Button(root, text="Down", command=lambda: [move_canvas_object("ufo", 0, 10), d_tri_incrementer()])
ufo_moveup_bt.grid(column=1,row=2)

ufo_moveup_bt = tk.Button(root, text="Left", command=lambda: [move_canvas_object("ufo", -10, 0), l_tri_incrementer()])
ufo_moveup_bt.grid(column=0,row=1)

ufo_moveup_bt = tk.Button(root, text="Right", command=lambda: [move_canvas_object("ufo", 10, 0), r_tri_incrementer()])
ufo_moveup_bt.grid(column=2,row=1)

ufo_beam = tk.Button(root, text="ABDUCT", command=create_triangle)
ufo_beam.grid(column=2,row=3)

ufo_beam_off = tk.Button(root, text="BEAM OFF", command=lambda: canvas_output.delete("beam"))
ufo_beam_off.grid(column=0,row=3)

def create_cow():
    """Even more tediously create a cow."""
    cow1 = canvas_output.create_rectangle(300,270,310,280, fill="white", outline="lightgrey")
    cow2 = canvas_output.create_rectangle(310,280,320,290, fill="white", outline="lightgrey")
    cow3 = canvas_output.create_rectangle(320,280,330,290, fill="white", outline="lightgrey")
    cow4 = canvas_output.create_rectangle(315,285,320,290, fill="black", outline="lightgrey")
    cow5 = canvas_output.create_rectangle(325,280,330,285, fill="black", outline="lightgrey")
    cowleg = canvas_output.create_rectangle(310,290,315,300, fill="white", outline="lightgrey")
    cowleg = canvas_output.create_rectangle(325,290,330,300, fill="white", outline="lightgrey")
    coweye = canvas_output.create_rectangle(305,270,310,275, fill="black", outline="lightgrey")

ground = canvas_output.create_rectangle(0,300,640,480, fill="darkgoldenrod4", tags="ground")
og_cow = create_cow()

#print(f"{ground}")
#print(inc)


root.mainloop()