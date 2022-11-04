"""
Ken Michna
Project 4 GUI

A test function for UFO GUI
"""
import tkinter as tk

import Project_4 as p4


def test_guiroot_is_tk():
    test_ufo = p4.Ufo()
    expected = tk.Tk()

    result = type(test_ufo.root) == type(expected)
    return result

def test_star_entry_box():
    test_ufo = p4.Ufo()
    test_ufo.star_entry_box.insert(0, "100")
    test_ufo.get_star_entry()

    test_var = test_ufo.desired_stars.get()
    comp_var = "Star Count:100"

    assert test_var == comp_var

print(test_guiroot_is_tk())
print(test_star_entry_box())