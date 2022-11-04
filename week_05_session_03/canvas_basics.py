import tkinter as tk

window = tk.Tk()

drawing = tk.Canvas(window, background="light blue", width=800, height=600)
drawing.grid(column=0, row=0)

# coords are in: x0, y0, x1, y1 format
rect1_id = drawing.create_rectangle(80, 50, 100, 500, fill="pink", outline="black")
# print(f"rect1_id: {rect1_id}")
rect1_coords = drawing.coords(rect1_id)
# print(f"rect1_coords: {rect1_coords}")

# modify our variable holding the data (Model) for the rectangle coords
# rect1_coords[0] = 40
# remember to update GUI (View) as well
# drawing.coords(rect1_id, rect1_coords)
# print(f"rect1_coords: {rect1_coords}")

#create a second canvas object!
rect2_id = drawing.create_rectangle(50, 150, 90, 400, fill="light green", outline="black")

def change_shape_outline(current_canvas, shape_id, outline_color):
    """Change shape with shape_id on current_canvas to have outline color of outline_color."""
    current_canvas.itemconfig(shape_id, outline=outline_color)

#create interaction panel
def reset_button_clicked():
    """Reset shape 1 on screen to initial coordinates."""
    drawing.moveto(1, rect1_coords[0], rect1_coords[1])

def move_button_helper(current_shape_id, x_move, y_move):
    # drawing.coords(current_shape_id, current_shape_coords)
    drawing.move(current_shape_id, x_move, y_move)

def move_button_clicked():
    """Move one shape over until it does not overlap with the other."""
    current_shape_id = 1
    opposing_shape_id = 2
    x_to_add = add_x_amount.get() # step before each check of shape overlapping
    y_to_add = add_y_amount.get()
    # validate entry number
    if x_to_add.isnumeric():
        x_to_add = int(x_to_add)
    else:
        print(f"x amount is invalid ({x_to_add})")
        return -1

    if y_to_add.isnumeric():
        y_to_add = int(y_to_add)
    else:
        print(f"y amount is invalid ({y_to_add})")
        return -1

    current_shape_coords = drawing.coords(current_shape_id)
    opposing_shape_coords = drawing.coords(opposing_shape_id)
    dx = int(current_shape_coords[0] - opposing_shape_coords[2]) #left of first box vs right of second box
    current_shape_initial_offset = -1 * int(dx)

    # update shape then check
    while dx <= 0:
        print(f"dx: {dx}")
        current_shape_coords[0] += x_to_add
        current_shape_coords[2] += x_to_add
        current_shape_coords[1] += y_to_add
        current_shape_coords[3] += y_to_add

        current_delay = 100*(current_shape_initial_offset + dx)

        # helper function so that we can use the .after method and that functionality that updates the GUI itself is in it's own function
        window.after(current_delay, move_button_helper, current_shape_id, x_to_add, y_to_add)

        #update dx
        # current_shape_coords = drawing.coords(current_shape_id)
        # opposing_shape_coords = drawing.coords(opposing_shape_id) # not moving, so we could reuse the old coord...
        dx = int(current_shape_coords[0] - opposing_shape_coords[2])
    # blink shape outline color to indicate that it is done moving
    window.after(current_delay, change_shape_outline, drawing, current_shape_id, "yellow")
    window.after(current_delay + 250, change_shape_outline, drawing, current_shape_id, "black")
    window.after(current_delay + 500, change_shape_outline, drawing, current_shape_id, "yellow")
    window.after(current_delay + 750, change_shape_outline, drawing, current_shape_id, "black")
    

reset_button = tk.Button(window, text="reset shapes", command=reset_button_clicked)
reset_button.grid(column=0, row=1)

move_button = tk.Button(window, text="add x", command=move_button_clicked)
move_button.grid(column=0, row=2)

add_x_amount_indicator = tk.Label(window, text="x amount")
add_x_amount_indicator.grid(column=1, row=1)
add_x_amount = tk.Entry(window)
add_x_amount.insert(0, "1")
add_x_amount.grid(column=1, row=2)

add_y_amount_indicator = tk.Label(window, text="y amount")
add_y_amount_indicator.grid(column=2, row=1)
add_y_amount = tk.Entry(window)
add_y_amount.insert(0, "0")
add_y_amount.grid(column=2, row=2)

window.mainloop()
