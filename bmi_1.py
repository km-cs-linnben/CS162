"""
File: bmi_1.py
Author: Ken Michna
Date: 4/9/2022

Description: Calculates BMI based off of user inputs of height(ft) and weight(lbs)
"""

height_ft = float(input("Enter your height in feet: "))
weight_lbs = float(input("Enter your weight in pounds: "))

m_in_ft = 3.2808        #meters in a foot
kg_in_lb = .454

height_m = height_ft / m_in_ft      #converts feet entered into meters
weight_kg = weight_lbs * kg_in_lb       #converts pounds entered into kilograms

bmi = weight_kg / height_m ** 2     #calculates BMI using metric measurements

print("Your BMI is: ",bmi)      #prints users BMI