import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

#input ; 07:05:45PM | output : 19:05:45

# """
# def timeConversion(s):
#     # Write your code here
#     if s[-2:] == "PM":
#         new = str(int(s[:2]) + 12) + s[2:-2]
        
#     else:
#         new = s[:-2]

#     return new
#     #return "{hr}{minsec}".format( hr = int(s[:2]) + (12 if s[-2:] =="PM" else 0), minsec = s[2:-2])#/
# """


from time import strptime, strftime
def timeConversion(s):
    return strftime("%H:%M:%S", strptime(s, "%I:%M:%S%p"))
    #strptime : datetime 형식 -> strftime : 시간 string 형식
    #%p는 AM/PM구분
    #%H :0~24시간 | %I: 0~12 시간

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

