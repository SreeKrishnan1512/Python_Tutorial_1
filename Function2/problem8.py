from datetime import datetime

''''
current_date = datetime.now()
current_month = current_date.month  # Returns the month as an integer (1-12)
print(f"Current Month: {current_month}")

'''

date=datetime(2024,12,15)

print(date.strftime("%a"))


'''
%A → Full weekday name (e.g., "Tuesday")
%a → Abbreviated weekday name (e.g., "Tue")
%w → Weekday as a number (0 for Sunday, 6 for Saturday)
print(date.strftime("%m"))  # Output: 12
print(date.strftime("%B"))  # Output: December
print(date.strftime("%b"))  # Output: Dec
'''
