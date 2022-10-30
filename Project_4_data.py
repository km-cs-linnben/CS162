"""
Ken Michna
Project 4 Representing Data

Collects list of numbers entered by user and sorts them. Has buttons to display lowest value number and a buttton
to iterate through the list of the numbers from smallest to largest values.

Need to figure out how to make sure user can not enter alpha characters. Entering alpha characters causes errors.
Also need to figure out how to make it not try to collect data from blank text boxes. Have tried numerous ideas and failed.

"""

import tkinter as tk

class Data_Gui:
    """GUI For Data Manipulation"""
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Data Sorting")

        # 10 seperate data entry boxes, made default values because repeatedly entering numbers while testing
        # was very annoying.
        self.box1 = tk.Entry(self.root)
        self.box1.grid(column = 1, row = 0)
        self.box1.insert(0, "10")
        self.box2 = tk.Entry(self.root)
        self.box2.grid(column = 1, row = 1)
        self.box2.insert(0, "9")
        self.box3 = tk.Entry(self.root)
        self.box3.grid(column = 1, row = 2)
        self.box3.insert(0, "8")
        self.box4 = tk.Entry(self.root)
        self.box4.grid(column = 1, row = 3)
        self.box4.insert(0, "7")
        self.box5 = tk.Entry(self.root)
        self.box5.grid(column = 1, row = 4)
        self.box5.insert(0, "6")
        self.box6 = tk.Entry(self.root)
        self.box6.grid(column = 1, row = 5)
        self.box6.insert(0, "5")
        self.box7 = tk.Entry(self.root)
        self.box7.grid(column = 1, row = 6)
        self.box7.insert(0, "4")
        self.box8 = tk.Entry(self.root)
        self.box8.grid(column = 1, row = 7)
        self.box8.insert(0, "3")
        self.box9 = tk.Entry(self.root)
        self.box9.grid(column = 1, row = 8)
        self.box9.insert(0, "2")
        self.box10 = tk.Entry(self.root)
        self.box10.grid(column = 1, row = 9)
        self.box10.insert(0, "1")

        #Labels for entry boxes, probably not needed but it looks prettier
        self.box1_label = tk.Label(self.root, text = "Box 1")
        self.box1_label.grid(column = 0, row = 0)
        self.box2_label = tk.Label(self.root, text = "Box 2")
        self.box2_label.grid(column = 0, row = 1)
        self.box3_label = tk.Label(self.root, text = "Box 3")
        self.box3_label.grid(column = 0, row = 2)
        self.box4_label = tk.Label(self.root, text = "Box 4")
        self.box4_label.grid(column = 0, row = 3)
        self.box5_label = tk.Label(self.root, text = "Box 5")
        self.box5_label.grid(column = 0, row = 4)
        self.box6_label = tk.Label(self.root, text = "Box 6")
        self.box6_label.grid(column = 0, row = 5)
        self.box7_label = tk.Label(self.root, text = "Box 7")
        self.box7_label.grid(column = 0, row = 6)
        self.box8_label = tk.Label(self.root, text = "Box 8")
        self.box8_label.grid(column = 0, row = 7)
        self.box9_label = tk.Label(self.root, text = "Box 9")
        self.box9_label.grid(column = 0, row = 8)
        self.box10_label = tk.Label(self.root, text = "Box 10")
        self.box10_label.grid(column = 0, row = 9)

        #List of all entry boxes to be used for iteration
        self.list_of_boxes = [self.box1, self.box2, self.box3, self.box4, self.box5, self.box6, self.box7, self.box8, self.box9, self.box10]
        self.list_of_entries = []
        self.itr_var = 0

        self.result_title = tk.Label(self.root, text = "Lowest Number Entered")
        self.result_title.grid(column = 2, row = 0)
        
        #Variable label, value changes to lowest number in list when button pressed
        self.result_label_var = tk.StringVar()
        self.lowest_number_label = tk.Label(self.root, textvariable = self.result_label_var)
        self.lowest_number_label.grid(column = 2, row = 1)

        #Button runs entry collection function and saves all entries to a list
        self.collect_button = tk.Button(self.root, text = "Collect All Entries", command=lambda: self.get_entries())
        self.collect_button.grid(column = 0, row = 10)

        #Button runs function to find lowest number then sets the label above it to that value
        self.find_lowest_button = tk.Button(self.root, text = "Find Lowest Number", command=lambda: self.result_label_var.set(self.get_lowest()))
        self.find_lowest_button.grid(column = 2, row = 2)

        #Variable label, value changes to current number in the list being iterated through
        self.iterate_label_var = tk.StringVar()
        self.iterate_return_label = tk.Label(self.root, textvariable = self.iterate_label_var)
        self.iterate_return_label.grid(column = 2, row = 4)

        #Button to iterate through list of entries, also sets label above it to the value
        self.iterate_button = tk.Button(self.root, text = "Iterate From Smallest to Largest", command=lambda: self.iterate_label_var.set(self.iterate()))
        self.iterate_button.grid(column = 2, row = 5)

        #Print button for debug
        self.printbutt = tk.Button(self.root, text = "print", command=lambda: self.print_test())
        self.printbutt.grid(column = 0, row = 11)
    
    def cleartext(self):
        """Clear text function for debugging test."""
        for box in self.list_of_boxes:
            box.delete(0, "end")

    def iterate(self):
        """Iterates through the collected list of entries"""
        output = self.list_of_entries[self.itr_var]
        self.itr_var += 1
        if self.itr_var > len(self.list_of_entries)-1:
            self.itr_var = 0
        return output

    def get_entries(self):
        """Collects user entries from every box."""
        if len(self.list_of_entries) != 10:
            for box in self.list_of_boxes:
                self.list_of_entries.append(int(box.get()))
        else:
            pass
        self.list_of_entries.sort()

    def get_lowest(self):
        """Gets lowest number from data boxes."""
        return self.list_of_entries[0]

    def print_test(self):
        """Prints list to assist in debug."""
        print(self.list_of_entries)

    def mainloop(self):
        self.root.mainloop()


def main():
    databoxes = Data_Gui()
    databoxes.mainloop()

if __name__ == "__main__":
    main()


