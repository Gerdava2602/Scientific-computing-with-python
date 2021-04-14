def add_time(start, duration, day=""):

  time_zone = ["PM", "AM"]
  days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

  times = start.split()
  hour = int(times[0].split(":")[0])
  minutes = int(times[0].split(":")[1])
  tz = times[1]

  if tz == "AM":
    tz_n = 1
  else:
    tz_n = 0

  add_hours = int(duration.split(":")[0])
  add_minutes = int(duration.split(":")[1])
  new_hours = (hour+add_hours+int((minutes+add_minutes)/60))%12
  tz_n = int((tz_n+(hour+add_hours+int((minutes+add_minutes)/60))/12)%2)


  if new_hours == 0:
    new_hours = 12
  

  new_minutes = (minutes+add_minutes) % 60
  later = ""
  if (hour+add_hours+int((minutes+add_minutes)/60))/24 < 1:
    new_days = 0
    if tz == "PM" and time_zone[tz_n] == "AM":
      new_days = 1
  else:
    new_days = round((hour+add_hours+int((minutes+add_minutes)/60))/24)

    
  if new_days == 1:
    later = " (next day)"
  elif new_days != 0:
    later = " ("+str(new_days)+ " days later)"

  if day == "":
    new_date = str(new_hours)+":"+"0"*(2-len(str(new_minutes)))+str(new_minutes)+" "+str(time_zone[tz_n])+ later
  else:
    day = finday(day, days)
    day = (day+new_days)%7

    new_date = str(new_hours)+":"+"0"*(2-len(str(new_minutes)))+str(new_minutes)+" "+str(time_zone[tz_n])+", "+days[day]+ later
    
  return new_date

def finday(day, days):
  i = 0
  for d in days:
    if d.lower() == day.lower():
      return i
    i += 1
  return None
