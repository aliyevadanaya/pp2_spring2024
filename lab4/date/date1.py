"""
Write a Python program to subtract five days from current date.
"""
import datetime
today = datetime.datetime.now()
result = today - datetime.timedelta(days=5)
print(result)
