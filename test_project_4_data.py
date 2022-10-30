"""
Ken Michna
Project 4 Data GUI Test Module

A couple test functions to test the Data GUI class methods.
"""

import tkinter as tk

from Project_4_data import Data_Gui

def test_sorting_and_get():
    datagui = Data_Gui()
    datagui.cleartext()
    
    datagui.box1.insert(0, "45")
    datagui.box2.insert(0, "4")
    datagui.box3.insert(0, "66")
    datagui.box4.insert(0, "98")
    datagui.box5.insert(0, "9")
    datagui.box6.insert(0, "11")
    datagui.box7.insert(0, "13")
    datagui.box8.insert(0, "33")
    datagui.box9.insert(0, "50")
    datagui.box10.insert(0, "42")

    datagui.get_entries()
    assert datagui.list_of_entries[0] == 4

def test_iterate_func():
    datagui = Data_Gui()
    datagui.list_of_entries = [1,2,3,4,5,6,7,8,9,10]
    datagui.iterate()
    datagui.iterate()

    assert datagui.itr_var == 2

def test_iterate_func2():
    datagui = Data_Gui()
    datagui.list_of_entries = [1,2,15,4,5,6,7,8,9,10]
    datagui.iterate()
    datagui.iterate()
    
    assert datagui.iterate() == 15

