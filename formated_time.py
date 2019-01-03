__author__ = 'Asmit'
import time
import calendar
localtime = time.asctime( time.localtime(time.time()))
print ("Local current time :", localtime)


# calender
cal  = calendar.month(2018,1)

print("Your calender")
print(cal)