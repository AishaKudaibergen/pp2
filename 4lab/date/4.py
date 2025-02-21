# Write a Python program to calculate two date difference in seconds

import datetime

date1_str = input("Enter the first date (YYYY-MM-DD): ")
date2_str = input("Enter the second date (YYYY-MM-DD): ")

try:
    first_date = datetime.datetime.strptime(date1_str, "%Y-%m-%d")
    second_date = datetime.datetime.strptime(date2_str, "%Y-%m-%d")
    
    difference = abs((second_date-first_date).total_seconds())

    print('Difference between the two dates in seconds:', int(difference))
except ValueError:
    print("Date format is incorrect, try again.")