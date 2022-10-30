"""
Ken Michna
Project 3
10/15/2022

I have a better idea of what I'm doing

Moveable UFO GUI with buttons to turn abduction beam on/off.
Added Star generation button. Generates the number of stars entered by user in random positions.
"""
import tkinter as tk
import random

from pyparsing import col

class Ufo:
    def __init__(self):
        """Initialize all components of UFO GUI"""
        self.root = tk.Tk()
        self.root.title("UFO")

        #Create blank canvas
        self.canvas_output = tk.Canvas(self.root, width=640, height=480, background="black", highlightbackground="purple")
        self.canvas_output.grid(column=0,row=4,columnspan=3)

        #Tediously create a UFO
        self.ufo = self.canvas_output.create_oval(110,10,250,50, fill="grey", outline="green", tags= "ufo")
        self.ufo_window = self.canvas_output.create_rectangle(115,25,125,35, fill="black", outline="green", tags="ufo")
        self.ufo_window1 = self.canvas_output.create_rectangle(145,25,155,35, fill="black", outline="green", tags="ufo")
        self.ufo_window2 = self.canvas_output.create_rectangle(175,25,185,35, fill="black", outline="green", tags="ufo")
        self.ufo_window3 = self.canvas_output.create_rectangle(205,25,215,35, fill="black", outline="green", tags="ufo")
        self.ufo_window4 = self.canvas_output.create_rectangle(235,25,245,35, fill="black", outline="green", tags="ufo")

        #Create increments to help abduction beam follow UFO
        self.yinc = 0
        self.xinc = 0

        #Generate the ground and a cow
        self.ground = self.canvas_output.create_rectangle(0,300,640,480, fill="darkgoldenrod4", tags="ground")
        self.og_cow = self.create_cow()

        #Control Buttons Suite
        self.ufo_moveup_bt = tk.Button(
        self.root, text="Up", command=lambda: [self.move_canvas_object("ufo", 0, -10), self.u_tri_incrementer(), self.beam_b_gone()])
        self.ufo_moveup_bt.grid(column=1,row=0)

        self.ufo_moveup_bt = tk.Button(
        self.root, text="Down", command=lambda: [self.move_canvas_object("ufo", 0, 10), self.d_tri_incrementer(), self.beam_b_gone()])
        self.ufo_moveup_bt.grid(column=1,row=2)

        self.ufo_moveup_bt = tk.Button(
        self.root, text="Left", command=lambda: [self.move_canvas_object("ufo", -10, 0), self.l_tri_incrementer(), self.beam_b_gone()])
        self.ufo_moveup_bt.grid(column=0,row=1)

        self.ufo_moveup_bt = tk.Button(
        self.root, text="Right", command=lambda: [self.move_canvas_object("ufo", 10, 0), self.r_tri_incrementer(), self.beam_b_gone()])
        self.ufo_moveup_bt.grid(column=2,row=1)

        self.ufo_beam = tk.Button(self.root, text="ABDUCT", command=self.create_triangle)
        self.ufo_beam.grid(column=2,row=3)

        self.ufo_beam_off = tk.Button(self.root, text="BEAM OFF", command=self.beam_b_gone)
        self.ufo_beam_off.grid(column=0,row=3)

        #Star Creation Suite
        self.desired_stars = tk.StringVar()
        self.star_label = tk.Label(self.root, textvariable = self.desired_stars)
        self.star_label.grid(column=3, row=0)
        self.desired_stars.set(f"Star Count: 0")
        self.star_entry_box = tk.Entry(self.root)
        self.star_entry_box.grid(column=3, row=1)

        #This button generates the desired number of stars and changes Star count label
        self.star_set_button = tk.Button(self.root, text ="*Generate Stars*", command=lambda: self.make_stars(self.get_star_entry()))
        self.star_set_button.grid(column=3, row=2)

        self.clear_stars_button = tk.Button(self.root, text = "Clear Stars", command=lambda: self.canvas_output.delete("stars"))
        self.clear_stars_button.grid(column=3, row=3)


    def mainloop(self):
        self.root.mainloop()
    
    def get_star_entry(self):
        """Returns number from desired_stars entry box and rewrites Stars label """
        self.desired_stars.set(f"Star Count:{self.star_entry_box.get()}")
        return int(self.star_entry_box.get())

    def make_stars(self, stars = 100):
        """Make star background"""
        for i in range(1,stars):
            starpointx = random.randint(0,630)
            starpointy = random.randint(0,470)
            star = self.canvas_output.create_oval(starpointx,starpointy,starpointx+5,starpointy+5, fill="white", tags="stars")
            self.canvas_output.lower(star,"ufo")

    def move_canvas_object(self, object_index, move_x, move_y):
        """Made into a function so buttons commands can do more than 1 thing at a time"""
        self.canvas_output.move(object_index, move_x, move_y)

    def create_triangle(self):
        """Creates a triangle underneath UFO."""
        self.yinc
        self.xinc
        points = [180+self.xinc,50+self.yinc,230+self.xinc,250+self.yinc,130+self.xinc,250+self.yinc]   #points in x/y coords per point for creating a triangle
        my_triangle = self.canvas_output.create_polygon(points, fill="green2", outline="blue", tags="beam")
        self.canvas_output.lower(my_triangle,self.og_cow)   #lowers triangle image 1 layer below cow

    def l_tri_incrementer(self):
        """Increments position left"""
        self.xinc -= 10

    def r_tri_incrementer(self):
        """Increments position right"""
        self.xinc += 10

    def u_tri_incrementer(self):
        """Increments position up"""
        self.yinc -= 10

    def d_tri_incrementer(self):
        """Increments position down"""
        self.yinc += 10

    def create_cow(self):
        """Even more tediously create a cow."""
        self.cow1 = self.canvas_output.create_rectangle(300,270,310,280, fill="white", outline="lightgrey")
        self.cow2 = self.canvas_output.create_rectangle(310,280,320,290, fill="white", outline="lightgrey")
        self.cow3 = self.canvas_output.create_rectangle(320,280,330,290, fill="white", outline="lightgrey")
        self.cow4 = self.canvas_output.create_rectangle(315,285,320,290, fill="black", outline="lightgrey")
        self.cow5 = self.canvas_output.create_rectangle(325,280,330,285, fill="black", outline="lightgrey")
        self.cowleg = self.canvas_output.create_rectangle(310,290,315,300, fill="white", outline="lightgrey")
        self.cowleg = self.canvas_output.create_rectangle(325,290,330,300, fill="white", outline="lightgrey")
        self.coweye = self.canvas_output.create_rectangle(305,270,310,275, fill="black", outline="lightgrey")

    def beam_b_gone(self):
        self.canvas_output.delete("beam")

def main():
    game = Ufo()
    game.mainloop()

if __name__=="__main__":
    main()

