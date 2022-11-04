"""
File: perfect_square.py
Author: Ken Michna
Date: 4/9/2022

Description: Prompts user for a number and prints whether it is a perfect square or not
"""
import math
number = int(input("Enter a number: ")) 

while number % math.sqrt(number) != 0:                               #if the numbers square root is not a nice whole number it will not divide into
    print(number,"is not a perfect square")                          #the number evenly. There will always be a remainder. If there is a remainder
    number = int(input("Try again: "))                               #the number is not a perfect square

print(number, "is a perfect square")
