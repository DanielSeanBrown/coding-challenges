#!/bin/python3

import math
import os
import random
import re
import sys

def sum_of_multiples(k, n):
    m = (n - 1) // k
    return k * m * (m + 1) // 2


if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        print(sum_of_multiples(3, n) + 
              sum_of_multiples(5, n) -
              sum_of_multiples(15, n))
