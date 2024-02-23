# Write a Python program to calculate two date difference in seconds.

import datetime
date1 = input() #YYYY-MM-DD HH:MM:SS
date2= input()
result1 = datetime.datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
result2 = datetime.datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")

difference = result2 - result1
difference_seconds = abs(difference.total_seconds())
print(difference_seconds)
