# Write a Python program to drop microseconds from datetime.
import datetime
today = datetime.datetime.now()
result = today.replace(microsecond=0)
print(result)
