# Write a Python program that invoke square root function after specific milliseconds
import math
import time
num = float(input())
vremya = float(input())
t = vremya/1000
time.sleep(t)
print(f"Square root of {num} after {vremya} miliseconds is {math.sqrt(num)}")
