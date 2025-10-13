#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
# 1 4 4 4 5 3

def migratoryBirds(arr):
    bird_types = [0] * 6
    for ar in arr:
        bird_types[ar] += 1
    print(bird_types)
    max_value = 0
    bird_id = 0
    for i in range(1, 6):
        if bird_types[i] > max_value:
            max_value = bird_types[i]
            bird_id = i
    return bird_id
            
print(migratoryBirds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]))
print(migratoryBirds([1, 4, 4, 4, 5, 3]))