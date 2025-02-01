# import the date class
from datetime import *

  
my_date = date(1996, 12, 11)
  
print("Date passed as argument is", my_date)

today = date.today()
  
print("Today's date is", today)

date_time = datetime.fromtimestamp(1887639468)
print("Datetime from timestamp:", date_time)


today = date.today()
    
# Converting the date to the string
Str = date.isoformat(today)
print("String Representation", Str)
print(type(Str))

  
Time = time(11, 34, 56)
  
print("hour =", Time.hour)
print("minute =", Time.minute)
print("second =", Time.second)
print("microsecond =", Time.microsecond)


# Using current time
ini_time_for_now = datetime.now()
  
# printing initial_date
print("initial_date", str(ini_time_for_now))
  
# Calculating future dates
# for two years
future_date_after_2yrs = ini_time_for_now + timedelta(days=730)
  
future_date_after_2days = ini_time_for_now + timedelta(days=2)
  
# printing calculated future_dates
print('future_date_after_2yrs:', str(future_date_after_2yrs))
print('future_date_after_2days:', str(future_date_after_2days))
