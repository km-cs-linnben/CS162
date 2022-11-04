hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
totalmin=(hour*60)+mins+dura
newhour=(round(totalmin/60))%24
newmin=totalmin%60
print("Duration",newhour,newmin,sep=":")
