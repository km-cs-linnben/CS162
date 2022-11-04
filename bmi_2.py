"""
File: bmi_2.py
Author: Ken Michna
Date: 4/9/2022

Description: This programs tells the user whether they are fat or not based off their calculated BMI
"""

height_ft = float(input("Enter your height in feet: "))
weight_lbs = float(input("Enter your weight in pounds: "))

m_in_ft = 3.2808        #meters in a foot
kg_in_lb = .454

height_m = height_ft / m_in_ft      #converts feet entered into meters
weight_kg = weight_lbs * kg_in_lb       #converts pounds entered into kilograms

bmi = weight_kg / height_m ** 2     #calculates BMI using metric measurements


if bmi < 18.5:                      #Finds users CDC's BMI rating based of previous BMI calculation
    print("You are underweight")
elif 18.5 <= bmi <= 24.9:
    print("You are normal")
elif 25.0 <= bmi <= 29.9:
    print("You are overweight")
else:
    print("You are obese :( ")

print("Your BMI is: ",round(bmi,2))      #prints users BMI rounded to 2 decimal places