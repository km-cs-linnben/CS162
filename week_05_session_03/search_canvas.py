import tkinter as tk
import random

window = tk.Tk()

drawing = tk.Canvas(window, background="light blue", width=400, height=150)
drawing.grid(column=0, row=0)

# coords are in: x0, y0, x1, y1 format
num_shapes = 10
shape_width = 10
shape_gap = 10
shape_height_minimum = 10
# shape_height_step = 10
random_shape_height = 10 # default value?
shape_height_maximum = 120
x_offset = 10
y_offset = 10
shape_ids = []
delay_step = 250 # delay for graphical updates
for count in range(num_shapes):
    random_shape_height = random.randint(shape_height_minimum, shape_height_maximum)
    current_shape_id = drawing.create_rectangle(
        (shape_width + shape_gap) * count + x_offset,
        shape_height_maximum + y_offset,
        (shape_width + shape_gap) * count + shape_width + x_offset,
        shape_height_maximum - random_shape_height + y_offset,
        fill="pink",
        outline="black")
    #should we track those object ids as well?
    left = (shape_width + shape_gap) * count + x_offset + 5
    bottom = shape_height_maximum + y_offset + 10
    drawing.create_text(left, bottom, text=f"{random_shape_height}")
    shape_ids.append(current_shape_id)

def change_shape_fill(current_canvas, shape_id, fill_color):
    """Change shape with shape_id on current_canvas to have fill color of outline_color."""
    current_canvas.itemconfig(shape_id, fill=fill_color)

#create interaction panel
def search_button_clicked():
    # get value from search entry
    #validate user input!
    value = int(search_value_entry.get())

    # walk through list of shape ids, checking if that id in the canvas has a height that matches the search value 
    # and highlight any that do match
    for count, shape_id in enumerate(shape_ids):
        current_coords = drawing.coords(shape_id)
        current_shape_height = current_coords[3] - current_coords[1]
        # print(f"shape_id ({shape_id}) has coords: {current_coords}, " +
        #       f"\n\twhich means it has a height of: " +
        #       f"{current_shape_height}")
        
        #check height of single shape versus search value
        if value == current_shape_height:
            # print(f"shape_id ({shape_id}) has coords: {current_coords}, " +
            #   f"\n\twhich means it has a height of: " +
            #   f"{current_shape_height}, which matches the search value!")
            window.after(count*delay_step, change_shape_fill, drawing, shape_id, "green")
        else:
            window.after(count*delay_step, change_shape_fill, drawing, shape_id, "red")
        
    #indicate that we are done!
    window.after(count*delay_step, done_indicator_stringvar.set, "done!")
    

done_indicator_stringvar = tk.StringVar("")
done_indicator = tk.Label(window, textvariable=done_indicator_stringvar)
done_indicator.grid(column=1, row=0)

search_button = tk.Button(window, text="search", command=search_button_clicked)
search_button.grid(column=0, row=2)

search_value_indicator = tk.Label(window, text="search value")
search_value_indicator.grid(column=1, row=1)
search_value_entry = tk.Entry(window)
search_value_entry.insert(0, "1")
search_value_entry.grid(column=1, row=2)


window.mainloop()
