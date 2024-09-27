import time
timestrap = time.strftime("%H:%M:%S")
print(timestrap)
timehour = int(time.strftime("%H"))
print(timehour)
timeminute = int(time.strftime("%M"))
print(timeminute)
timesecond = int(time.strftime("%S"))
print(timesecond)
if(timehour>=0 and timehour<12):
    print("good morning sir")
elif(timehour>=12 and timehour<17):
    print("good afternoon sir")
elif(timehour>=17 and timehour<=20):
    print("good evening sir")
else:
    print("good night sir")