import sys
from datetime import *

def convert_to_military(time):
    """ Return time in military format. """
    tmp = datetime.strptime(time, "%I:%M:%S%p")
    return datetime.strftime(tmp, "%H:%M:%S")

if __name__ == '__main__':
    time = sys.stdin.readline().strip()

    print convert_to_military(time)
