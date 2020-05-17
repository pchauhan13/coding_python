import sys

try:
    answer = 0/0
except:
    print(sys.exc_info())
