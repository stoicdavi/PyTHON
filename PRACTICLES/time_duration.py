hour = int(input("Enter the starting time of the meeting(hours)"))
minutes = int(input("Enter the minutes of the hour(minutes)"))
duration = int(input("Enter the time duration of your meeting(minutes)"))
minutes = minutes + duration
hour +=minutes//60 #Find the number of hours hidden in the minutes and update the hour
hour = hour%24 #correct the hour to make sure it lies btn 0...24hrs
minutes%=60 
print(hour,":",minutes,sep="",end="\n")
