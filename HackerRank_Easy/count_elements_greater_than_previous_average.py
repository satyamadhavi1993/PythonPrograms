import math
import os
import random
import re
import sys

#
# Complete the 'countResponseTimeRegressions' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY responseTimes as parameter.
#

def countResponseTimeRegressions(responseTimes):
    total = count = 0
    for i in range(1, len(responseTimes)):
        total += responseTimes[i - 1]
        if responseTimes[i] > total / i:
            count += 1
    return count
        
        
if __name__ == '__main__':
    responseTimes = [100, 200, 150,300]
    result = countResponseTimeRegressions(responseTimes)
    print(result)
    responseTimes = []
    result = countResponseTimeRegressions(responseTimes)
    print(result)
    responseTimes = [1, 2, 3]
    result = countResponseTimeRegressions(responseTimes)
    print(result)
