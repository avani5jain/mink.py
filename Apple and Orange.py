import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    x=0
    y=0
    c=0
    d=0
    for i in range(0,len(apples)):
        x=a+apples[i]
        if(x>=s and x<=t):
            c=c+1
    for j in range(0,len(oranges)):
        y=b+oranges[j]
        if(y>=s and y<=t):
            d=d+1
    
    print(c)
    print(d)
if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
