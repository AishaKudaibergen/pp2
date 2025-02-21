# Write a Python program to subtract five days from current date.
import datetime

today = datetime.datetime.today()

five_days_before = today - datetime.timedelta(days=5)

print("Five days from current date:", five_days_before)