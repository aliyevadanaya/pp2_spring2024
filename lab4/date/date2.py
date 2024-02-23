"""Write a Python program to print yesterday, today, tomorrow."""
import datetime
today = datetime.datetime.today()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)
print(yesterday)
print(today)
print(tomorrow)