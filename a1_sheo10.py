#!/usr/bin/env python3

import os
import sys

def leap_year(obj):
    while True:
        is_leap_year = None
        year = int(obj)
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    is_leap_year = True
                else:
                    is_leap_year = False
            else:
                is_leap_year = True
        else:
            is_leap_year = False
        if is_leap_year:
            return True
        else:
            return False

def sanitize(obj1,obj2):
    results = ""
    for char in obj1:
        if char in obj2:
            results += char
    return results

def size_check(obj, intobj):
    status = False
    if len(obj) == intobj:
        status = True
    return status

def range_check(obj1, obj2):
    status = False
    if int(obj1) in range(obj2[0],obj2[1]+1):
        status = True
    return status

def usage():  
 status = "Usage: a1_sheo10.py YYYYMMDD|YYYY/MM/DD|YYYY-MM-DD|YYYY.MM.DD"

 return status

if __name__ == "__main__":
   # step 1
   if len(sys.argv) != 2:
      print(usage())
      sys.exit()
   # step 2
   month_name = ['Jan','Feb','Mar','Apr','May','Jun',
                 'Jul','Aug','Sep','Oct','Nov','Dec']
   days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
                    7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
   user_raw_data = sys.argv[1]
   # step 3
   allow_chars = '0123456789'
   dob = sanitize(user_raw_data, allow_chars)
#   print('Sanitized user data:', dob)
   # setp 4
   result = size_check(dob,8)
   if result == False:
       print("Error 09: wrong date entered")
       sys.exit()
   # step 5
   year = int(dob[0:4])
   month = int(dob[4:6])
   day = int(dob[6:])
   # step 6
   result = range_check(year,(1900,9999))
   if result == False:
       print("Error 10: year out of range, must be 1900 or later")
       sys.exit()
   result = range_check(month,(1,12))
   if result == False:
       print("Error 02: wrong month entered")
       sys.exit()
   result = leap_year(year)
   if result == True:
       days_in_month[2] = 29
   result = range_check(day, (1, days_in_month[month]))
   if result == False:
       print("Error 03: wrong day entered")
       sys.exit()
   # step 7
   new_dob = str(month_name[month - 1])+' '+ str(day)+', '+str(year)
   # step 8
   print(new_dob)
#   print("Your date of birth is:", new_dob)  



