import time
#(year, month, day, hours, min, sec, day of the week, day of the year, summer time)
print(time.ctime(0)) #print epoch, as reference point.
print(time.ctime(1000000000))

print(time.time()) #retun current seconds since epoch
print(time.ctime(time.time())) #the local time using above functions, one inside the other
print()

time_object = time.localtime()
print(time_object) #This is not readable...so...
# see the directives in the manual
local_time = time.strftime("%d %B %Y %H:%M:%S", time_object)
print(local_time)
print()

birthday_string = "18 April, 1985"
birthday_object = time.strptime(birthday_string, "%d %B, %Y")
print(birthday_object)
print()

time_tuple = (1985, 4, 18, 0, 0, 0, 0, 0, 0)
btday_string = time.asctime(time_tuple)
print(btday_string)