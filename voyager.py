"""
File: voyager.py
Author: Ken Michna
Date: 4/1/2022
Description: Program evaluates how far the Voyager space probe is from Earth
"""

mfe = 16637000000       #How far Voyager is from Earth in miles on Sept 25,2009
speedmph = 38241        #Voyager speed in miles per hour
kilo_per_mile = 1.609344        #Number of kilometers in 1 mile
mile_per_au = 92955887.6        #Number of miles in 1 AU
radiowave = 179875474.8     #Speed of radio waves in kilometers per hour

days = int(input("Enter number of days after Sept 25, 2009: "))     #Find number of days since baseline

dfsun_mile = days * 24 * speedmph + mfe        #Distance from Sun in miles after number of days passed
dfsun_kilo = dfsun_mile * kilo_per_mile      #Distance from sun in kilometers
dfsun_au = dfsun_mile / mile_per_au     #Distance from sun in AU
radio_trv = (dfsun_kilo / radiowave) * 2     #Round trip travel time of radio wave from Earth to Voyage

print("The distance from the Sun in miles is: ", dfsun_mile)
print("The distance from the sun in kilometers is: ", dfsun_kilo)
print("The distance fron the sun is AU is: ", dfsun_au)
print("The round trip travle time of a radio wave to Voyager is: ", radio_trv, "hours")





