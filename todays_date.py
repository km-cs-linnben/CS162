"""
File: todays_date.py
Author: Ken Michna
Date: 4/1/2022
Description: Displays my name and the current date.
"""

from datetime import datetime

print("Name: Ken Michna")
print("Today's date: ",datetime.today().strftime('%Y-%m-%d'))